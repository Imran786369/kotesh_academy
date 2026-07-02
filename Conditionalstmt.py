# marks=int(input("Enter your marks : "))
# if marks>90:
#     print('A Grade')
# elif marks>80 and marks<=90:
#     print('B Grade')
# elif marks>70 and marks<=80:
#     print('C Grade')
# elif marks>60 and marks<=70:
#     print('D Grade')
# else:
#     print('Invalid Grade')
userName=input('Enter username')
password=input('Enter your password')
if userName=='kdkr' and password=='1234':
    print('Sucessfully logged in')
elif userName=='kdkr' and password!='1234':
    print('Enter correct password')
elif userName!='kdkr' and password=='1234':
    print('Enter correct username')
else:
    print('Invalid credentials')
