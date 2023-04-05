# name = input('enter your name:> ')
# age = int(input('enter your age:> '))

# if age < 8:
#     print(f'{name}, you are kid.')
# elif 8 <= age < 13:
#     print(f'{name}, you are junior')
# elif 13 <= age < 18:
#     print(f'{name}, you are teenager.')

# else:
#     print(f'{name}, you are adult.')

# برنامه ای بنویسید که دو عدد را از ورودی دریافت نماید
# یکی از عملگرهای ریاضی زیر را از ورودی بگیرد
# +     -      *      /       //
# در نهایت خروجی محاسبه را نمایش دهد.


# دیکشنری   dictionary

favorite_sports = ["football", "tennis", "baseball", "pingpong"]

favorite_sports = {
    'sobhan': 'football',
    'danial': 'football',
    'mehrzad': 'basketball',
    'ayrana': 'tennis'
}

print(f"ayrana likes {favorite_sports['ayrana']}")
print(f'sobhan likes {favorite_sports["sobhan"]}')

favorite_sports['mahdi'] = 'pingpong'
del favorite_sports['sobhan']
print(favorite_sports)


favorite_sports = {}
name = input('enter a name:> ')
sport = input('enter sport:> ')
favorite_sports[name] = sport
print(favorite_sports)
#  تمرین
# غذاهای مورد علاقه دوستانتان را در دیکشنری ذخیره کنید و نمایش دهید
