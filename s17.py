# for i in range(1,11):
#     print(i)
# for i in range(2,11,2):
#     print(i)
# تمرین 1
# اعداد فرد را با کمک حلقه فور بسازید
# for i in range(10,0,-1):
#     print(i)
# for i in range(3):
#     print("a")
# for j in range(3):
#     print("b")
# for i in range(3):
#     print("a")
#     for j in range(3):
#         print("b")

# total = 0

# for i in range(3):
#     new_number = int(input('enter a number: '))
#     total = total + new_number

# print("total is: ", total)

# تمرین 2
'''
برنامه ای بنویسید که پنج عدد از ورودی دریافت نماید و تعداد اعدادی که صفر هستند را نمایش دهد
'''

number_of_zeros = 0
zero_numbers = []
for i in range(5):
    new_number = int(input('enter a number:> '))
    if new_number == 0:
        zero_numbers.append(new_number)
        # number_of_zeros += 1

print("number of zeros:", number_of_zeros)
print("number of zeros:", len(zero_numbers))



# import turtle
# COLORS = ['black','green','blue','cyan']
# s = turtle.Screen()
# s.bgcolor('orange')
# p = turtle.Pen()
# p.pensize(2)
# p.speed('fast')
# p.pencolor("red")
# p.shape('turtle')
# p.shapesize(2)
# for i in range(4):
#     p.fillcolor(COLORS[i])
#     p.begin_fill()
#     for i in range(4):
#         p.forward(100)
#         p.left(90)
#     p.end_fill()

#     p.left(90)
# کشیدن مستطیل
# for i in range(2):
#     p.forward(200)
#     p.left(90)
#     p.forward(100)
#     p.left(90)
# s.exitonclick()





# while