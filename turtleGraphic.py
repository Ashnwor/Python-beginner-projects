# @Author: ashnwor
# @Date:   03-Nov-2018
# @Email:  ashnwor@gmail.com
# @Last modified by:   ashnwor
# @Last modified time: 03-Nov-2018
# Create graphic based on input using turtle library

import turtle
import random
import time

# Define dimensions
x = 800
y = 800
xAxis = -270
normalSpeed = 3

turtle.setup(x, y)
window = turtle.Screen()
window.bgcolor("black")
window.title("Graphic! WoHoOoOoOo!")
turtle.pencolor("white")
turtle.speed(0)
turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()
turtle.goto(-300, -300)
turtle.goto(300, -300)
turtle.penup()
turtle.goto(0, 350)
turtle.write("such graphic!", align="center", font=("Arial", 12, "normal"))
turtle.setpos(-330, -200)
turtle.write("100")
turtle.setpos(-330, -100)
turtle.write("200")
turtle.setpos(-330, 0)
turtle.write("300")
turtle.setpos(-330, 100)
turtle.write("400")
turtle.setpos(-330, 200)
turtle.write("500")
turtle.setpos(-330, 300)
turtle.write("600")
turtle.setpos(-300, -300)
turtle.speed(normalSpeed)
turtle.pendown()

while True:
    randVar = random.randint(1, 601)
    variable = randVar-300
    print("DEBUG:", "variable:", variable)
    turtle.goto(xAxis, variable)
    turtle.pencolor("lightgreen")
    turtle.speed(0)
    turtle.write(randVar, align="center", font=("Arial", 10, "bold"))
    turtle.goto(xAxis, variable)
    turtle.pencolor("white")
    turtle.speed(normalSpeed)
    xAxis = xAxis+30
    print("DEBUG:", "xAxis:", xAxis)
    if xAxis == 330:
        time.sleep(1)
        turtle.hideturtle()
        time.sleep(1)
        break

input("Enter to terminate")
