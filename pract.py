import random
import turtle
c=turtle.Screen()
c.bgcolor("black")
c.title("Neon Mandala")

t=turtle.Turtle()

color=["red","orange","yellow","lime","violet","pink","cyan"]
for i in range(80):
    t.color(random.choice(color))
    t.forward(i*2)
    t.right(91)
    
    
t.penup()
t.goto(0,-60)
t.setheading(90)
t.pendown()
t.color("yellow")
t.begin_fill()
for i in range(5):
    t.forward(130)
    t.right(144)

t.end_fill()

t.penup()
t.goto(0,0)
t.pendown()

for i in range(36):
    t.color(random.choice(color),random.choice(color))
    t.begin_fill()
    for j in range(4):
        t.forward(55)
        t.right(90)
    t.end_fill()
    t.right(10)



turtle.done()