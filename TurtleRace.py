import turtle
import random

screen = turtle.Screen()

screen.bgcolor("lightblue")
screen.title("Turtle Race!")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]
turtles = []
start_y = 100

# Create turtles
for color in colors:
    turtleRacer = turtle.Turtle()
    turtleRacer.color(color)
    turtleRacer.shape("turtle")
    turtleRacer.penup()
    turtleRacer.goto(-100, start_y)
    turtleRacer.pendown()

    turtles.append(turtleRacer)
    start_y -= 50


# Draw finish line
finish_line_x = 100
line = turtle.Turtle()
line.penup()
line.goto(finish_line_x, 110)
line.right(90)
line.pendown()
line.forward(380)

#turtle movement
winner = None
while not winner:
    for turtleRacer in turtles:
        turtleRacer.forward(random.randint(1,5))
        if turtleRacer.xcor() >= finish_line_x:
            winner = turtleRacer
            break

#declare winner
message=turtle.Turtle()
message.hideturtle()
message.penup()
message.goto(-200,100)
message.color(winner.pencolor())
message.write(winner.pencolor().capitalize() + " Wins ", font=("Arial", 15, "bold"))
turtle.done()