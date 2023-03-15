# USERNAME = 'admin'
# PASS = 'root'


# user_name = input('enter user name:> ')
# password = input('enter password:> ')

# if user_name == USERNAME and password == PASS:
#     print('user name and password is valid.')
#     print('login was successful')
# else:
#     print("user name or password is not correct.")
#     print('login failed...')


a = 4
b = 5
c = 6


# if a < b:
#     print("a is less than b")
# if a > b:
#     print("a is greater than than b")
# if a <= b:
#     print("a is less than or equal to b")
# if a >= b:
#     print("a is greater than or equal to b")

a = 4
b = 5
c = 6

# if a < b and a < c:
#     print("a is less than b and c")

# if a < b or a < c:
#     print("a is less than either a or b (or both)")

# a = True
# if a:
#     print("a is true")
# if not a:
#     print("a is false")


# a = True
# b = False
# if a and b:
#     print("salaam")


# a = 3
# b = 3
# c = a == b
# print(c)


# if 1:
#  print("1")

# if 0:
#  print('0')

# if "A":
#  print("A")

# if "":
#  print("some thing")

USERNAME = ['admin', 'root']
PASSW = 'root'

user_name = input('enter user name:> ')
password = input('enter password:> ')

if user_name and password:
    if user_name == USERNAME and password == PASSW:
        print("account is valid")
        print("login was successful")
    else:
        print("user name or password is not correct")

else:
    print('you must enter user name and password')


# برنامه با لا را به گونه ای اصلاح کنید که هر دو نام کاربری را بتوان وارد نمود
# یعنی اگر نام کاربری اول یا نام کاربری دوم را وارد نماید
# و کلمه عبور را نیز وارد نماید، لاگین موفقیت آمیز باشد
