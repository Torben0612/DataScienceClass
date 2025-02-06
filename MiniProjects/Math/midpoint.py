import math
x1 = int(input('Enter X Value for point 1'))
y1= int(input('Enter Y Value for point 1'))
x2 = int(input('Enter X Value for point 2'))
y2 = int(input('Enter Y Value for point 2'))

midpoint = ((x2-x1)/(y2-y1))
distance = math.sqrt((x2-x1) + (y2-y1))

print('The midpoint: ' + str(midpoint))
print('The distance: ' + str(distance))