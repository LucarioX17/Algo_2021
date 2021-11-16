import turtle

t = turtle.Turtle()

for i in range(200):
    t.forward(5+i)
    t.right(15)

turtle.exitonclick()