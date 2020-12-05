import turtle
t=turtle.Pen()
t.color("white")
wn=turtle.Screen()
wn.bgcolor("black")
t.begin_fill()
t.fillcolor("red")
# t.speed(0)
for x in range(100):
    t.forward(2*x)
    t.left(75) #ansle

t.end_fill()
t.hideturtle()
