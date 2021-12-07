import turtle

t = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]

turtle.delay(0)

for i in range(6):
    t[i].penup()
    t[i].goto(-200, 250 - (100 * i))
    t[i].pendown()
    t[i].hideturtle()

def vonKoch(n, distance, i):
    if (n == 0):
        t[i].forward(distance)
    else:
        vonKoch(n-1, distance/3, i)
        t[i].left(60)
        vonKoch(n-1, distance/3, i)
        t[i].right(120)
        vonKoch(n-1, distance/3, i)
        t[i].left(60)
        vonKoch(n-1, distance/3, i)

for i in range(6):
    vonKoch(1 + i, 400, 0 + i)

turtle.exitonclick()