import turtle
import random

rohaan = turtle.Turtle()
umair = turtle.Turtle()

colors = ["red", "blue", "green", "yellow", "orange", "purple","pink", "brown", "gray", "cyan"]
positions = [-200, -150, -100, -50, 0, 50, 100, 150, 200,250]


all_turtles = []
for i in range(10):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-300, positions[i])
    all_turtles.append(t)



for i in range(200):
    for t in all_turtles:
        t.forward(random.randint(1,5))
        if t.xcor() >= 300:
            t.write("Winner!", font=("Arial", 20, "bold"))
            turtle.done()


turtle.done()
