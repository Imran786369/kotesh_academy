#Using Direct Assignment
# lst = [1, 2, 3, 4, 5]
# lst[0],lst[-1]=lst[-1],lst[0]
# print(lst)

#Using Tuple Variable
lst = [1, 2, 3, 4, 5]
pair=lst[-1],lst[0]
lst[0],lst[-1]=pair
print(lst)

#Using the * Operator
lst = [1, 2, 3, 4, 5]
a, *mid, b=lst
lst=[b, *mid, a]
print(lst)