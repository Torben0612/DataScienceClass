import math
unknown_side = input("Which side type is Unknown (side or hypotenuse")

if unknown_side == "side":
    a = int(input("Enter value of a: "))
    c = int(input("Enter value of c"))
    b = math.sqrt(a**2 + c**2)
    print("The unkown side length is: " + str(b))
elif unknown_side == "hypotenuse":
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of c"))
    c = math.sqrt(a**2 + b**2)
    print("The hypotenuse side length is: " + str(c))
else:
    print("Invalid side name (type either side or hypotenuse)")