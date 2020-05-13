from turtle import Turtle, Screen
from itertools import cycle
from random import randrange

MAX_TURTLES = 20
LANE_WIDTH = 25
FONT_SIZE = 18
FONT = ("Arial", FONT_SIZE, "normal")
COLORS = cycle(['red', 'green', 'blue', 'cyan', 'black', 'yellow'])
FINISH_LINE = 350
START_LINE = -200
NAME_LINE = START_LINE - 150
DELAY = 100  # milliseconds
MAX_STEP = 10
turtles = dict()

def race():
    for name, turtle in turtles.items():  # should shuffle turtles
        turtle.forward(randrange(MAX_STEP + 1))

        if turtle.xcor() > FINISH_LINE:
            return  # the race is over

    screen.ontimer(race, DELAY)

magic_marker = Turtle(visible=False)
magic_marker.penup()

turtNum = 0
while not 1 <= turtNum <= MAX_TURTLES:
    turtNum = int(input('Enter the number of turtles: '))

for i in range(turtNum):

    name = input('Enter a name for the turtle #{}: '.format(i + 1))

    turtle = Turtle(shape="turtle")
    turtle.color(next(COLORS))

    y_offset = LANE_WIDTH * i - LANE_WIDTH * turtNum // 2

    magic_marker.color(turtle.pencolor())
    magic_marker.goto(NAME_LINE, y_offset - FONT_SIZE / 2)
    magic_marker.write(name, font=FONT)

    turtle.penup()
    turtle.goto(START_LINE, y_offset)
    turtle.pendown()

    turtles[name] = turtle

magic_marker.color('red')
magic_marker.goto(FINISH_LINE, -FINISH_LINE)
magic_marker.pendown()
magic_marker.goto(FINISH_LINE, FINISH_LINE)
magic_marker.penup()

screen = Screen()

screen.ontimer(race, DELAY)

screen.exitonclick()
