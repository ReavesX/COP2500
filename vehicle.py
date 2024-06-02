# Donald Jackson - Vehicle.py - Create a simple vehicle using the turtle library - 02/07/22

#initializing
import turtle as t
my_screen = t.getscreen()
my_turtle = t.Turtle()
my_turtle.pensize(4)
my_turtle.setheading(0)
my_screen.bgcolor("blue")


#Starting to draw the actual design of the vehicle

my_turtle.pencolor("red")
my_turtle.begin_fill()
my_turtle.fillcolor("red")
my_turtle.forward(120)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(150)
my_turtle.right(90)
my_turtle.forward(25)
my_turtle.right(90)
my_turtle.forward(25)
my_turtle.right(-90)
my_turtle.forward(25)
my_turtle.end_fill()

#Adding some wheels
my_turtle.pencolor("black")
my_turtle.penup()
my_turtle.goto(20,-45)
my_turtle.pendown()
my_turtle.begin_fill()
my_turtle.fillcolor("black")
my_turtle.circle(15)
my_turtle.penup()
my_turtle.goto(120,-45)
my_turtle.pendown()
my_turtle.circle(15)
my_turtle.end_fill()
