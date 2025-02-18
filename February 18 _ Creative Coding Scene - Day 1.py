import turtle
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()

#ADD CODE HERE
wn.bgcolor("#ADD8E6")  #changes the background colour
t.speed(10) #speed of the turtle

t.penup()
t.right(90) #start of green grass
t.forward(200)
t.right(90)

t.pencolor("green") #colour of the pen
t.pendown() #pendown for drawing of grass
t.forward(370)
t.back(715)
t.right(90) #rotates 3 times ("t.right(90)" x3)
t.right(90)
t.right(90)
t.forward(125)
t.right(90)
t.forward(700) # longs
t.right(90)
t.forward(125)

t.pencolor("black") #colour of the pen
t.penup()
t.right(90)
t.forward(130)
t.left(90)

t.pendown() #start of cottage
t.forward(200)
t.right(90)


#last line of code
wn.exitonclick()


# t.fillcolor("#5bb450") #tree
