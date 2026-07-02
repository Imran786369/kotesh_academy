#Using deque.rotate() from collections
# from collections import deque
# arr = [12, 10, 5, 6, 52, 36]
# k=2
# d=deque(arr)
# d.rotate(-k)
# print(list(d))

# #Using List Slicing
# arr = [12, 10, 5, 6, 52, 36]
# k=2
# arr=arr[k:]+arr[:k]
# print(arr)

#Using extend()
arr = [12, 10, 5, 6, 52, 36]
k=2

x=arr[:k]
y=arr[k:]
y.extend(x)
print(y)
