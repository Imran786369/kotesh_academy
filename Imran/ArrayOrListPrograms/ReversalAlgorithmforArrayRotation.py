#Using reverse() Function
# arr = [1, 2, 3, 4, 5, 6, 7]
# d=2
# n=len(arr)

# #Reverse first d elements
# arr[:d]=reversed(arr[:d])

# #Reverse remaining elements
# arr[d:]=reversed(arr[d:])
# arr.reverse()
# print(arr)

#Using collections.deque
from collections import deque
arr = [1, 2, 3, 4, 5, 6, 7]
d=2
res=deque(arr)
res.rotate(-d)
print(list(res))


