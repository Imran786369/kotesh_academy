#Using Built-in max() Function
# arr = [10, 324, 45, 90, 9808]
# res=max(arr)
# print("Maximum element in an array", res)

#Using Iteration
# arr = [10, 324, 45, 90, 9808]
# max=arr[0]
# for i in range(1,len(arr)):
#     if arr[i]> max :
#         max=arr[i]
# print("Largest number in an array: ", max)

#Using reduce() Function
# from functools import reduce
# arr = [10, 324, 45, 90, 9808]
# max=reduce(max,arr)
# print("Largest number in an array: ", max)

#Using sort() Function
# arr = [10, 324, 45, 90, 9808]
# arr.sort()
# res=arr[-1]
# print('Largest number in an array : ',res)

#Using operator.gt()
import operator
arr = [10, 324, 45, 90, 9808]
res=0
for i in arr:
    if operator.gt(i,res):
        res=i
print(res)
