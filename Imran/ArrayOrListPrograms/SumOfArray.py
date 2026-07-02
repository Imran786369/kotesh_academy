#Using sum() Function
# arr=[10,23,6,12]
# ans=sum(arr)
# print('Sum : ',ans)

#Using reduce() Method
# from functools import reduce
# arr=[10,23,6,12]
# ans=reduce(lambda a,b:a+b,arr)
# print('Sum : ',ans)

#Using Iteration
# arr=[10,23,6,12]
# t=0
# for x in arr:
#     t+=x
# print('Sum :', t)

#Using enumerate() Function
arr=[10,23,6,12]
t=0
for i,val in enumerate(arr):
    t+=val
print('Sum : ',t)
