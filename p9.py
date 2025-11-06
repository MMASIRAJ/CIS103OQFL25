def acres():
    try:
        h = float(0.4047)
        a = float(input('Enter acres: '))
        ac = a * h
        print(a,'Converts to ', ac, 'hectares')
    except ValueError:
        print('Value Error')
    except TypeError:
        print('Type Error')
    except:
        print('Unknown Error')

def Quarts():
    try:
        L = float(0.946353)
        Q = float(input('Enter Quarts: '))
        li = L * Q
        print(Q, 'Converts to ', li, 'Liters')
    except ValueError:
        print('Value Error')
    except TypeError:
        print('Type Error')
    except:
        print('Unknown Error')

def fah():
    try:
        
        F = float(input('Enter Fahrenheit: '))
        
        K = ((F-32)*(5/9)+273.15)
        
        print (F, 'Convert to ', K, 'Kelvin')
    except ValueError:
        print('Value Error')
    except TypeError:
        print('Type Error')
    except:
        print('Unknown Error')
    
def main():
    again = 'y'
    while((again == 'y') or (again == 'Y')):
        acres()
        print('-----------------')
        Quarts()
        print('-----------------')
        fah()
        print('-----------------')
        again = input('Again (y/n):')
    print('--done--')
    
main()
    
    
    
    
