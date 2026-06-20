def Area_Of_Circle(r) :
    pi = 3.14
    area = pi * r * r
    return area
radius = int(input("Enter radius of the circle: "))
areaOfCircle= Area_Of_Circle(radius)
print("Area of Circle:", areaOfCircle)
