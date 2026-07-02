# a=('mango','banana','apple','orange','apple')
# print(type(a))
# a=list(a)
# a.append(input("Enter fruit name :"))
# print(type(a))
# print(a)
# print(a[0])
# print(a[2])
# print(a[-2])
# print(a[-1])
# a[-1]='grapes'
# print(a)
# print(a.index('apple'))
# for i in a:
#     print(i, ':', len(i))
    
# a={}
# for i in range(10):
#     a.update({i:i**2})
# print(a.keys())
# print(a.values())
# print(a.items())

# a={'city':'hyd',
#    'year': 2026}
# # a['state']='Telengana'
# a.update({'state':'Andhra Pradesh'})
# print(a)
# a={}
# # a={i:i**2 for i in range(10) if i%2 == 0}
# a={i:i**2 if i%2 == 0 else 'invalid' for i in range(10)}
# print(a)

a={'city':'Hyderabad',
   'state':'Telengana',
   'year': 2026}
b={}
# for i,j in a.items():
#     b.update({i:type(j)})
#     print(b)
b={i:len(j) for i,j in a.items()}
print(b)