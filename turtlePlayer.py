# @Author: ashnwor
# @Date:   03-Nov-2018
# @Email:  ashnwor@gmail.com
# @Last modified by:   ashnwor
# @Last modified time: 03-Nov-2018
import turtle

window = turtle.Screen()
window.bgcolor("black")
player = turtle.Turtle()
player.speed(0)


def turnLeft():
    player.left(15)


def turnRight():
    player.right(15)


def goForward():
    player.forward(10)


def drawSonDraw():
    turtle.pendown()


def dontDraw():
    turtle.penup()


def main():
    player.color("white")
    player.shape("triangle")
    player.penup()
    turtle.listen()
    turtle.onkeypress(turnLeft, "a")
    turtle.onkeypress(turnRight, "d")
    turtle.onkeypress(goForward, "w")
    turtle.onkey(drawSonDraw, "space")
    turtle.onkeyrelease(dontDraw, "space")

    input()


main()
