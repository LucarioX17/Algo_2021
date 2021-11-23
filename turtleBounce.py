import turtle, random

t = []

turtle.delay(0)
width = 800
height = 800
screen = turtle.Screen()
screen.setup(width, height)

amount = 5

def randomColor():
    color = "%06x" % random.randint(0, 0xFFFFFF)
    return color

def createCirle(i):
    t.append(turtle.Turtle())
    t[i].fillcolor("#" + str(randomColor()))
    t[i].penup()
    t[i].goto(random.randint(-(width/2), width/2), random.randint(-(height/2), height/2))
    t[i].shape("circle")
    t[i].shapesize(3)
    t[i].right(random.randint(1, 360))

for i in range(amount):
    createCirle(i)

while True:
    for i in range(amount):
        t[i].forward(0.5)

        if (t[i].xcor() > width/2 or t[i].xcor() < -(width/2) or t[i].ycor() > height/2 or t[i].ycor() < -(height/2)):
            t[i].right(45)

        #if (random.randint(1, 1000) > 999):
        #    t[i].right(random.randint(1, 360))

turtle.exitonclick()