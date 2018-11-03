import turtle

x = 600
y = 600
turtle.setup(x, y)
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Hey!")
turtle.hideturtle()
turtle.penup()
turtle.pencolor("white")
turtle.pensize(3)
turtle.left(90)
turtle.forward(150)
turtle.pendown()
turtle.goto(150.00, 0.00)
turtle.goto(0.00, -150.00)
turtle.goto(-150.00, 0.00)
turtle.goto(0.00, 150.00)
print(turtle.pos())
input("Exit this shit up")
