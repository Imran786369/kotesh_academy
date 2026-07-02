def Arithmetic_Ops(a,b):
    sum = a+b
    difference = a-b
    multiplication = a*b
    division = a/b
    return sum, difference, multiplication, division
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

Addition, Subtraction, Multiplication, Division = Arithmetic_Ops(x, y)
print("Addition :", Addition)
print("Subtraction :", Subtraction)
print("Multiplication :", Multiplication)
print("Division :", Division)