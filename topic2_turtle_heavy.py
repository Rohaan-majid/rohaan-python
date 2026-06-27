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



screen = turtle.Screen()

# Track finish order
finished = []
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

max_iters = 10000
iters = 0
while iters < max_iters:
    iters += 1
    for t in all_turtles:
        if t in finished:
            continue
        t.forward(random.randint(1,15))
        if t.xcor() >= 300:
            finished.append(t)
            t.penup()
            # When first finisher appears, show top-center winner text
            if len(finished) == 1:
                winner_color = t.pencolor()
                top_y = screen.window_height() / 2 - 40
                writer.goto(0, top_y)
                writer.color(winner_color)
                writer.write(f"The winner is {winner_color}", align="center", font=("Arial", 24, "bold"))

            # When we have 3 finishers, draw podium and stop the race
            if len(finished) >= 3:
                # Podium layout
                top_y = screen.window_height() / 2 - 40
                # lower the podium so it doesn't overlap the winner text
                podium_y = top_y - 160
                podium_width = 80
                # heights for 1st,2nd,3rd
                heights = [80, 60, 40]
                xs = [0, 120, -120]  # 1st center, 2nd right, 3rd left

                drawer = turtle.Turtle()
                drawer.hideturtle()
                drawer.penup()
                drawer.goto(0, podium_y)
                drawer.pendown()
                drawer.color("black")

                # draw simple podium rectangles
                for i, h in enumerate(heights[::-1]):
                    # draw from left to right: 3rd,2nd,1st for nicer ordering
                    pass

                # Place top-3 turtles on podium and label them
                places = [(0, heights[0]), (120, heights[1]), (-120, heights[2])]
                labels = ["1st", "2nd", "3rd"]
                for idx in range(3):
                    tfin = finished[idx]
                    px, ph = places[idx]
                    # position turtle on top of its podium
                    tfin.goto(px, podium_y + ph + 10)
                    tfin.setheading(0)
                    tfin.showturtle()
                    # write label below the turtle
                    label_writer = turtle.Turtle()
                    label_writer.hideturtle()
                    label_writer.penup()
                    label_writer.goto(px, podium_y + ph + 30)
                    col = tfin.pencolor()
                    label_writer.color(col)
                    label_writer.write(f"{labels[idx]}: {col}", align="center", font=("Arial", 14, "bold"))

                # hide all other turtles
                for oth in all_turtles:
                    if oth not in finished[:3]:
                        oth.hideturtle()

                turtle.done()

    # safety: stop if all finished
    if len(finished) == len(all_turtles):
        break

turtle.done()
