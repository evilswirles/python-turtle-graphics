import turtle
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()

#ADD CODE HERE
wn.bgcolor("#191970")  #changes the background colour
t.pencolor("white") #colour of the pen
t.speed(5) #speed of the turtle


t.forward(100)
t.back(50)
t.right(90)
t.forward(100)


#last line of code
wn.exitonclick()
