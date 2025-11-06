def run():
    minutes = input('Enter Running Time: ')
    
    if minutes.isspace() or minutes == "":
        print('Running time cannot be blank')
        return None
    elif int(minutes) <= 5:
        print('Running time must be greater than 5')
        return None
    else:
        return int(minutes)

def cal(minutes):
    c = 4.33  
    a = 0
    
    while a < minutes:
        a += 5
        calories_burned = a * c
        print('Minutes:', a, 'Calories burned:', calories_burned)


ans = 'y'
while ans.lower() == 'y':
    mins = run()
    if mins:
        cal(mins)
    ans = input('Do you want to calculate again? (y/n): ')

