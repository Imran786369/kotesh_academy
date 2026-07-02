def My_avg(a,b,c) :
    if c>=40 :
        my_average = (a+b+c)/3
        return my_average
    else :
        print("Average cannot be calculated as c is less than 40") 
x=int(input("Enter x value: "))
y=int(input("Enter y value: "))
z=int(input("Enter z value: "))
average = My_avg(x, y, z)
print("Average:", average)
