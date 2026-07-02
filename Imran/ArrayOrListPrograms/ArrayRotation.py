#Using List Slicing
# arr = [1, 2, 3, 4, 5, 6]
# d=2
# arr[:]=arr[d:]+arr[:d]
# print(arr)

#Using reverse() Method
# arr = [1, 2, 3, 4, 5, 6]
# d=2
# n=len(arr)
# arr.reverse()
# arr[:n-d]=arr[:n-d][::-1]
# arr[n-d:]=arr[n-d:][::-1]
# print(arr)

#Using Temporary Array
# arr = [1, 2, 3, 4, 5, 6]
# d=2
# n=len(arr)

# temp=arr[:d]
# arr[:n-d]=arr[d:]
# arr[n-d:]=temp
# print(arr)

#One by One Rotation
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n=len(arr)
for i in range(d):
    arr.append(arr.pop(0))
print(arr)