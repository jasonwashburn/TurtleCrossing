from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.car_list = []
        self.new_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        new_car = Turtle(shape='square')
        new_car.color(choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_len=2)
        new_car.setx(280)
        new_car.sety(randint(-250, 250))
        self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            new_x = car.xcor() - self.car_speed
            car.setx(new_x)

    def flush_cars(self):
        for car in self.car_list:
            if car.xcor() < -320:
                self.car_list.remove(car)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
