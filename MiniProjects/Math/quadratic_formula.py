import math

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

discriminant = b ** 2 - 4 * a * c
if discriminant != 1:
    print("Not a real number")
else:
    quadratic1 = (-b + math.sqrt(discriminant)) / (2 * a)
    quadratic2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("answer: " + str(quadratic1) + " " + str(quadratic2))