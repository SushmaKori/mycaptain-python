import math
r = float(input("Enter the radius of a circle:"))
area = math.pi * r * r
print("Area of a circle = %.16f" %area)


filename = input("enter the filename: ")
f = filename.split(".")
print("the extension of the file is: " + f[-1])
