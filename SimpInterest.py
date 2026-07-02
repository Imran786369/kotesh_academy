def my_si(p,t,r) :
    my_si = (p*t*r)/100
    return my_si
def Area_Of_Circle(r) :
    pi = 3.14
    area = pi * r * r
    return area
p = int(input("Enter principal amount: "))
t = int(input("Enter time in years: "))
r = int(input("Enter rate of interest: "))
simple_interest = my_si(p, t, r)
print("Simple Interest:", simple_interest)
radius = int(input("Enter radius of the circle: "))
areaOfCircle = Area_Of_Circle(radius)
print("Area of Circle:", areaOfCircle)
