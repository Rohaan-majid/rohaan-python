import turtle
import random

rohaan = turtle.Turtle()
umair = turtle.Turtle()


rohaan.shape("turtle")
umair.shape("turtle")


rohaan.color("green")
umair.color("blue")


rohaan.penup() # do not draw line when moving
umair.penup()

rohaan.goto(-300,0)
umair.goto(-300,-50)



for i in range(200):
    rohaan.forward(random.randint(1,5))
    umair.forward(random.randint(1,5))


turtle.done()
