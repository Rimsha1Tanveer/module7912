import turtle
import random

# Screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala")

# Turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Colors
colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink"]

# 1. Outer Spiral
for i in range(80):
    t.color(random.choice(colors))
    t.forward(i * 2)
    t.right(91)

# 2. Filled Star
t.penup()
t.goto(0, -60)
t.setheading(90)
t.pendown()

t.color("yellow")
t.begin_fill()

for i in range(5):
    t.forward(130)
    t.right(144)

t.end_fill()

# 3. Filled Squares
petal_colors = ["cyan", "lime", "violet", "orange", "pink"]

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(36):

    t.color(random.choice(petal_colors),random.choice(petal_colors))

    t.begin_fill()

    for j in range(4):
        t.forward(55)
        t.right(90)

    t.end_fill()

    t.right(10)

turtle.done()