import math

#Area of a Rectangle
width = int(input('Enter width: '))
Height = int(input('Enter height: '))
Area = width * Height
print('Area of rectangle is: ', Area)

#Area of traingle is: area = 1/2 times base times height
base = int(input('Enter the base: '))
H = int(input('Enter the height: '))
a = float(1/2*base*H)
print('Area of traingle is: ', a)

#Area of a circle
Radius = float(input('Enter the radius: '))
ar = float(3.1459*Radius**2)
print('Area of circle is: ', ar)
