print('-----Start program-----')
print('\n')

print('Choose your number: ')
add = print('01. Add')
Sub = print('02. Subtract')
mul = print('03. Multiply')
div = print('04. Divide')

choice = input('enter choice number 1,2,3 or 4:')

for aa in range(1,2,1):
    i = float(input('Enter a number: '))
     
    for bb in range(1,11,1):
        if(choice=='1'):
            print(float(bb + i), '=', i, '+', bb)
            
        elif (choice=='2'):
            print(float(i - bb), '=', i, '-', bb)
            
        elif (choice=='3'):
            print(float(bb * i), '=', i, '*', bb)
            
        elif (choice=='4'):
            print(float(i / bb), '=', i, '/', bb)
        else:
            print('error')

print('\n')
print('-----done')
