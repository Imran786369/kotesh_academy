# 1. Python Syntax
# if 100>2:
#     print("100 is greater than 2")
#     print("try again")
# else:
#     print("100 is not greater than 2")
    
# 2. Python Variables
a=9

#3 Python comments
# This is a single-line comment
""" sdsd
asdsdd
sdsd
"""
# a1 = '25'
# b1 = "Kandukur"
# results = a1 + b1
# print(results)
a = "KOTESH ACADEMY KANDUKUR"
# count = 0
# for i in a:  #For loop to iterate through each character in the string 'a'
#     if i == 'A':  #If the character is 'K', it will be printed
#         count = count + 1  #Increment the count variable by 1 each time 'K' is found
#     # print(i)
# print("Number of 'A' characters:", count)
# b=a[15:]
# b=a[:6]
# b=a[-23:-16]
# print(b)
#For loop
fruits=['apple','banana','orange','mango']
kdkr = [] 
for i in fruits:
    for j in i:
        if j=='a':
            if i not in kdkr:
                kdkr.append(i)
        # if i%3==0:
            # kdkr.append(i)
            # print(i)
print(kdkr)