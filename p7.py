def kilometers():
    miles = input('Enter Total Miles: ')
    if (miles.isspace()):
        print('Miles cannot be blank')
    elif (miles.isalpha()):
        print('Miles cannot be alpha')
    elif not miles:
        print('Miles cannot be blank')
    else:
        m = float(miles)
        kilo = (m * 1.609344)
        print(m, 'miles in kilometers: ', kilo)

def weight():
    pound = input('Enter number of pounds: ')
    if (pound.isspace()):
        print('pounds cannot be blank')
    elif (pound.isalpha()):
        print('Pounds cannot be alpha')
    elif not pound:
        print('Pounds cannot be blank')
    else:
        p = float(pound)
        kg = float(p * 0.45349237)
        print(p, 'pounds in kiolgrams: ', kg)

def tem():
    fah = input('Enter temperature in fahrenheit: ')
    if (fah.isspace()):
        print('fahrenheit cannot be blank')
    elif (fah.isalpha()):
        print('Fahrenheit cannot be alpha')
    elif not fah:
        print('Fahrenheit cannot be blank')
    else:
        f = float(fah)
        celcius = float((f - 32)* 5/9)
        print(f, 'fahrenheit in celcius: ', celcius)
def cal():
    kilometers()
    weight()
    tem()

cal()
