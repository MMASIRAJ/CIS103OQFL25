def main():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    rainfall = []  

    print("Enter rainfall for Chicago (2017):")
    for month in months:
        while True:
            value = input(f"{month}: ")

            if value.strip() == "":
                print("Error: cannot be blank.")
                continue

            try:
                amount = float(value)
            except:
                print("Error: must be a number.")
                continue
            
            if amount < 0:
                print("Error: amount cannot be negative.")
                continue

            rainfall.append(amount)
            break

    
    highest = max(rainfall)
    lowest = min(rainfall)
    total = sum(rainfall)
    average = total / len(rainfall)

    
    high_month = months[rainfall.index(highest)]
    low_month = months[rainfall.index(lowest)]

    print("\n--- RESULTS ---")
    print(f"Highest:  {high_month}  {highest}")
    print(f"Lowest:   {low_month}  {lowest}")
    print(f"Total:    {total}")
    print(f"Average:  {average:.2f}")


main()
