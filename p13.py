def d():
    num = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi',
           7: 'vii', 8: 'viii', 9: 'ix', 10: 'x', 11: 'xi', 12: 'xii',
           13: 'xiii', 14: 'xiv', 15: 'xv', 16: 'xvi', 17: 'xvii', 18: 'xviii',
           19: 'xix', 20: 'xx', 21: 'xxi', 22: 'xxii', 23: 'xxiii', 24: 'xxiv'}
    
    try:
        a = 'y'
        while (a == 'y' or a == 'Y'):
            number = int(input('Enter a number:'))
            if number in num:
                print(number, 'in Roman is', num[number])
                a = input('Do you need to continue: (y or n)')
            elif (number <= 0 ):
                print('number must be above 0')
                break
            else:
                a = input('Key not found. Do you need to add a key,(y or n)')
                if (a == 'n'):
                    print('done')
                    break
                else:
                    try:
                        if number not in num:
                            newroman = str(input('Enter roman number'))
                            num[number] = newroman
                            print(num)
                            a = input('Do you need to continue: (y or n)')
                        else:
                            print('Number is already in keylist')
                    except ValueError:
                        print('Value Error')
                        break
                    except KeyError:
                        print('Key Error')
                        a = input('do you need to continue? y/n')
    except ValueError:
        print('Value Error')
    except KeyError:
        print('Key Error')
    
        
    
        
d()
    
