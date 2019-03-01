from turtle import *
shape("turtle")
color ("green", "yellow")
begin_fill()
for i in range(20):
    for j in range(20):
        left(1)
        forward(1)
end_fill()
mainloop()