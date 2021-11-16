import turtle, random

turtle.delay(0)

t = [turtle.Turtle(), turtle.Turtle()]

t[0].color("blue")
t[1].color("red")


while True:
    t[0].right(random.randint(1, 360))
    t[0].forward(random.randint(1, 100))

    t[1].right(random.randint(1, 360))
    t[1].forward(random.randint(1, 100))

turtle.exitonclick()