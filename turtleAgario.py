import turtle, random, time

t = []
sizes = []

turtle.delay(0)
width = 1000
height = 800
screen = turtle.Screen()
screen.setup(width, height)

amount = 10
amountJ = amount

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
    i=0
    while i<amount:
        t[i].forward(0.5)

        if (t[i].xcor() > width/2 or t[i].xcor() < -(width/2) or t[i].ycor() > height/2 or t[i].ycor() < -(height/2)):
            t[i].right(180)

        if (random.randint(1, 1000) > 999):
            t[i].right(random.randint(1, 360))

        j=0
        while j<amountJ:
            xx = 0
            yy = 0
            if (i != j):
                xx = t[j].xcor()
                yy = t[j].ycor()

            if (sizes[i] > sizes[j]):
                if (i < len(t) and j<len(t) and t[i].xcor() < xx + (sizes[i]*8) and t[i].xcor() > xx - (sizes[i]*8)):
                    if (t[i].ycor() < yy + (sizes[i]*8) and t[i].ycor() > yy - (sizes[i]*8)):
                        sizes[i] += sizes[j]
                        t[i].shapesize(sizes[i])
                        t[j].hideturtle()
                        t[j].clear()
                        t.remove(t[j])
                        amountJ -= 1
                        amount -= 1
            j+=1
        i+=1         
        

turtle.exitonclick()