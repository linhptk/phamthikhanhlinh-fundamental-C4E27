# 1
# def say_helloworld():
#     for i in range(3):
#         print("Hello World")
# say_helloworld()

# 2
# def add_two_number(a,b):
#     print(a+b)
# add_two_number(5,5)

# 3
# from turtle import *
# shape("turtle")
# def draw_shapes(length,line_color):
#     color(line_color)
#     for i in range(4):
#         forward(length)
#         left(90)
# draw_shapes(100,"blue")

# 4
# from turtle import *
# shape("turtle")
# def draw_square(length,line_color):
#     color(line_color)
#     for i in range(4):
#         forward(length)
#         left(90)
# for i in range(30):
#     draw_square(i * 5, 'red')
#     left(17)
#     penup()
#     forward(i * 2)
#     pendown()

# 5
# from turtle import *
# shape("turtle")
# def draw_star(x,y,length):
#     color("blue")
#     penup()
#     setposition(x,y)
#     pendown()
#     for i in range(5):
#         forward(length)
#         left(144)
#     mainloop()
# draw_star(-80,80,100)


# 6
# from turtle import *
# shape("turtle")
# def draw_star(x,y,length):
#     penup()
#     setposition(x,y)
#     pendown()
#     for i in range(5):
#         forward(length)
#         right(144)
#     mainloop()
# draw_star(-80,80,100)
# speed(0)
# color('blue')
# for i in range(100):
#     import random
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     length = random.randint(3, 10)
#     draw_star(x, y, length)

def remove_dollar_sign(s):
    new_string = (s.replace("$",""))
    return new_string

# 7
# Using: replace and transalate function()
# s = asdfgh
# print(s.replace("a", "")) --> replace function
# prit(s.translate({ord("a"): None})) --> Transalate function
#  
# 