radius = int(input("Type a circle radius that I will give you the area: "))
pi = 3.14

def calculateArea(x, y):
    area = y * (x * x)

    print("The area = " + str(area))

calculateArea(radius, pi)

