import turtle
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()

#ADD CODE HERE
wn.bgcolor("#191970")  #changes the background colour
t.pencolor("white") #colour of the pen
t.speed(5) #speed of the turtle


def snowflake_1(): #snowflake 1
    t.right(60)
    t.forward(100)
    t.penup()
    t.back(100)
    t.pendown()


i = 0
while i < 6:
    snowflake_1()
    i += 1

t.penup()
t.forward(150)
t.pendown()


t.forward(60)
t.back(30)
t.right(90)
t.forward(30)
t.back(60)
t.forward(30)
t.right(30)
t.forward(30)
t.back(60)
t.back(30)

#last line of code
wn.exitonclick()
