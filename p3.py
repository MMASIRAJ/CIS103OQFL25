#  Ahamed Siraj Mohamed Munir
#Simple Sales invoice
pound = float(input('Enter number of pounds to be purchased: '))
Gross = float(pound*0.99)
d1 = float(Gross * 0.1)
d2 = float(Gross * 0.2)
d3 = float(Gross * 0.3)
d4 = float(Gross * 0.4)

if (0 <= pound <= 9.99):
    print('Gross Sales: ', Gross)
    print('Discount: ')
    print('Final Amount: ', Gross)
elif (10 <= pound <= 99.99):
    print('Gross Sales: ', Gross)
    print('Discount: ', d1)
    print('Final Amount: ', Gross * 0.9)
elif (100 <= pound <= 999.99):
    print('Gross Sales: ', Gross)
    print('Discount: ', d2)
    print('Final Amount: ', Gross - d2)
elif (1000 <= pound <= 9999.99):
    print('Gross Sales: ', Gross)
    print('Discount: ', d3)
    print('Final Amount: ', Gross - d3)
elif (10000 <= pound):
    print('Gross Sales: ', Gross)
    print('Discount: ', d4)
    print('Final Amount: ', Gross - d4)
else:
    print('Pounds must be greater than 0')
    
    









