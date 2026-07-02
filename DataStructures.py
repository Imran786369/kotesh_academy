# a=['mango',53,63.14,True,53,'kandukur','mango',29,'kdkr']  #define list
# # print(a[-3:])  #indexing, ordered, slicing list
# a[0] = 'banana'  #list changeable
# print(a)
# # a[1:5] = ["bat"]
# a.insert(1, 'grapes')  #insert element in list
# print(a)
# a.remove('mango')  #remove element from list
# print(a)
# print(a.index('kandukur'))  #find index of element in list
# b=a.copy()  #copy list
# print(b)
# a.insert(7, 'chennai')  #insert element in list
# print(a)
# print(a.count('grapes'))  #count element in list
# print(a.pop(2))  #pop element from list
# a.extend(['apple', 'banana'])  #extend list
# print(a)
# a.reverse()  #reverse list
# print(a)

# a=['mango','banana','grapes','mango',58,63.14]
# # a[0]='pen'  #list changeable
# print(7%3)  #floor division

# for i in range(10):
#     print(i)  #for loop

# x=int(input("Enter your number :"))
# if x%2==0:
#     print("its an even number")
# else:
#     print('its an odd number')

# for i in range(1,10):
    
#     if i%5 == 0:       
#         pass
#     print(i)

# a=int(input("Enter your number : "))
prime_bucket=[]
non_prime_bucket=[]
for a in range(100):
    if a>1:
    
        for i in range(2,a):
            if a%i == 0:
                non_prime_bucket.append(a)
                print(a, " : Its not a prime number")
                break
        else:
            prime_bucket.append(a)
            print(a, ' : its a prime number')
    else:
         non_prime_bucket.append(a)
         print(a, " : Its not a prime number")
print('Prime numbers are : ', prime_bucket)
print("Non Prime numbers are : ", non_prime_bucket)

# a=[1,2,3,6]
# b=[7,8,9,10]
# a.extend(b)
# # a.append(100)
# # print(a)
# # a.append('apple')
# print(a)
# b.extend(a)
# print(b)
# a=[1,2,3,6]
# print(a.pop(1))
# # a[1]='mango'
# print(a)