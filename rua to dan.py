from turtle import *
speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
shape("turtle")
for n in range(3,8):
    color(colors[n-3])
    for i in range(n):
        forward(100)
        left(360/n)
mainloop()





















mainloop()