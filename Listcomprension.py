a=['mango','apple','banana','grapes']
b=[]
print(a)
a.sort()
print(a)
a.sort(reverse = True)
print(a)
a.reverse()
print(a)
a.remove('banana')
print(a)
a.pop(1)
print(a)
del a[0]
print(a)
a.clear()
print(a)
# for i in a:
#     if len(i)==5:
#         b.append(i)  
# print(b)

# b=[i for i in a if 'e' in i]
# print(b)
# b=['Yes' if 'e' in i else 'No' for i in a]
# print(b)