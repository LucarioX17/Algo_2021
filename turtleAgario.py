import turtle, random, time

t = []
sizes = []

turtle.delay(0)
width = 1000
height = 800
screen = turtle.Screen()
screen.setup(width, height)

amount = 2

def randomColor():
    color = "%06x" % random.randint(0, 0xFFFFFF)
    return color

def createCirle(i):
    t.append(turtle.Turtle())
    t[i].fillcolor("#" + str(randomColor()))
    t[i].penup()
    t[i].goto(random.randint(-(width/2), width/2), random.randint(-(height/2), height/2))
    t[i].shape("circle")
    size = random.randint(1, 5)
    sizes.append(size)
    t[i].shapesize(size)
    t[i].right(random.randint(1, 360))

for i in range(amount):
    createCirle(i)

while True:
    for i in range(amount):
        t[i].forward(0.5)

        if (t[i].xcor() > width/2 or t[i].xcor() < -(width/2) or t[i].ycor() > height/2 or t[i].ycor() < -(height/2)):
            t[i].right(180)

        for j in range(amount):
            xx = 0
            yy = 0
            if (i != j):
                xx = t[j].xcor()
                yy = t[j].ycor()

            if (t[i].xcor() > xx and t[i].xcor() + sizes[i]*2 < xx + sizes[j]*2):
                if (t[i].ycor() > yy and t[i].ycor() + sizes[i]*2 < yy + sizes[j]*2):
                    print(t[i].xcor(), t[i].ycor())
                    time.sleep(2)
                    
        if (random.randint(1, 1000) > 999):
            t[i].right(random.randint(1, 360))

turtle.exitonclick()