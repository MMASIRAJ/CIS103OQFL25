def number():
    while True:
        num = input('Enter a number:')
        if (num.isalpha()):
            print('Number cannot be alhabetic')
        elif (num.isspace()):
            print ('Number cannot be blank')
        elif (int(num) <= 0):
            print('Number cannot be less than 0')
        else:
            return int(num)

def fact(n):
    print('',n,end="")
    if n == 0:
        return 0
    else:
        return n + fact(n - 1)


def execution():
    print('------Sum up numbers------')
    ans = 'y'
    while (ans == 'y'):
        b = number()
        a = fact(b)
        print('Total Sum is :', a)
        ans = input('Do you want to continue (y/n):')

    print('---Done---')

execution()


