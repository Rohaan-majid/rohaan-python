# make varaible shape and assign it value "turtle"
# make variable color and assign it anny color like red or blue
# make variable and give it speed iteger value
# make variable step and give it value 100
# ..... angle and give it value 90
import turtle


shape = "turtle"
color = "green"
speed = 1.3
step = 100
angle = 90


turtle.shape(shape)
turtle.color(color)

for i in range(4):
    turtle.forward(step)
    turtle.left(angle)


# make triable with step 100 and angle 120
amgle=120
for i in range(3):
 turtle.forward(step)
 turtle.right(amgle)


turtle.mainloop()








