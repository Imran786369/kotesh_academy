# #Using Multiple Assignment
# a = [10, 20, 30, 40, 50]
# a[0],a[4]=a[4],a[0]
# print(a)

# #Using XOR Operator
# a = 5
# b = 10
# a=a^b
# b=a^b
# a=a^b
# print(a,b)

#Using a Temporary Variable
a = [10, 20, 30, 40, 50]
temp=a[2]
a[2]=a[4]
a[4]=temp
print(a)