# Hinh 1
# from turtle import *
# colors = ['red', 'blue', 'brown', 'yellow', 'grey']
# angle = [120,90,72,60,50]
# for i in range(5):
#     color(colors[i])
#     for j in range(i+3):
#         forward(100)
#         left(angle[i])

# Hinh 2
# Minh chua biet cach lam the nao de tach cac hinh chu nhat
from turtle import * 
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(5):
        color(colors[i])
        begin_fill()
        for j in range (4):
                forward(10)
                right(90)
                forward(100)
        end_fill()

