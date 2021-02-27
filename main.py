import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Turtle(shape='turtle')
turtle.color('black')
turtle.penup()
turtle.setheading(90)
turtle.goto(0, -280)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
