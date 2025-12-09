def main():
    print("--------------------------Program started----------------------")

    file_path = "C:/Users/ahame/OneDrive/Desktop/Associates Degree/CIS Electives/CIS 103/points.txt"
    file_path_02 = "C:/Users/ahame/OneDrive/Desktop/Associates Degree/CIS Electives/CIS 103/grades.txt"
    file_path_03 = "C:/Users/ahame/OneDrive/Desktop/Associates Degree/CIS Electives/CIS 103/errors.txt"
    infile = open(file_path, "r")
    grade_file = open(file_path_02, "w")
    error_file = open(file_path_03, "w")
    print('\n')
    read_count = 0
    error_count = 0
    good_count = 0
    A_count = 0
    B_count = 0
    C_count = 0
    D_count = 0
    F_count = 0

    line = infile.readline()

    while line != "":
        read_count += 1

        parts = line.split(',')
        ID = parts[0].strip()
        name = parts[1].strip()
        points_str = parts[2].strip()

        error_message = ""

        if not points_str.isnumeric():
             error_message = "Points must be numeric"
        else:
            points = int(points_str)

            if points < 0:
                error_message = "Points cannot be negative"
            elif points > 1000:
                error_message = "Points cannot be more than 1000"

        # Write to error or grade file
        if error_message != "":
            error_file.write(ID + "," + name + "," + points_str + "," + error_message + "\n")
            error_count += 1
        else:
            pct = points / 10

            if pct >= 90:
                grade = "A"
                A_count += 1
            elif pct >= 80:
                grade = "B"
                B_count += 1
            elif pct >= 70:
                grade = "C"
                C_count += 1
            elif pct >= 60:
                grade = "D"
                D_count += 1
            else:
                grade = "F"
                F_count += 1

            good_count += 1
            grade_file.write(ID + "," + name + "," + str(points) + "," + grade + "\n")

        line = infile.readline()

    infile.close()
    grade_file.close()
    error_file.close()
 
    print("Number of records read:", read_count, '\n')
    print("Number of A's:", A_count)
    print("Number of B's:", B_count)
    print("Number of C's:", C_count)
    print("Number of D's:", D_count)
    print("Number of F's:", F_count, '\n')
    print("Number of graded records:", good_count)
    print("Number of error records:", error_count, '\n')

    print("------------------------Program ended----------------------------")

main()

