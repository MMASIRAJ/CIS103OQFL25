# Ahamed Siraj Mohamed Munir
#validating payment data file

name = input('Name: ')
n = len(name)
        
if(name.isnumeric()):
    print('Name:       Name must be alphabet')
else:
    if (n==0)or (name.isspace()):
        print('Name: ', name, 'Name cannot be blank')
    else:
        if(3 > n):
            print('Name:       Name must be atleast 3 characters')
        else:
            print('Name: ', name, ' Valid')

account_number = input('Account number')
num = len(account_number)

if(account_number.isspace()):
    print('Account number cannot be blank')
else:
    if(num==0):
        print('Account number: ', account_number, 'Account number cannot be blank')
    
    else:
        if(account_number.isalpha()):
            print('Account number:           Account number must be numeric')
        else:
            
            if(1 <= num <= 9):
                print('Account number: ', account_number, 'Valid')
            else:
                print('Account number:         Account number must be atleast 9 digits')            

pay = input('payment: ')
p = len(pay)
       
if (pay.isspace()):
    print('payment:          Payment cannot have spaces')
else:
    if(p==0):
        print('Payment cannot be blank')
    else:
        pa = float(pay)
        if (1 <= pa):
            print('payment: ', pa, 'valid')
        else:
            print('pay cannot be zero or negative')
