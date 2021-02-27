import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, 'Up')

new_car_count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Detect when player reaches the top of the screen
    if player.ycor() > 300:
        player.refresh()

    # Create new car every 6 times the screen is refreshed
    if new_car_count == 6:
        car_manager.new_car()
        new_car_count = 0

    # Move the cars
    car_manager.move_cars()

    # Remove cars when they pass the edge of the screen
    car_manager.flush_cars()

    new_car_count += 1
