import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_up, 'w')


new_car_count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Detect when player reaches the top of the screen
    if player.ycor() > 300:
        player.refresh()
        scoreboard.level += 1
        scoreboard.update_score()
        car_manager.speed_up()

    # Detect car collisions
    for car in car_manager.car_list:
        if car.ycor() + 20 > player.ycor() > car.ycor() - 20:
            if car.xcor() - 20 < player.xcor() < car.xcor() + 20:
                game_is_on = False
                scoreboard.game_over()

    # Create new car every 6 times the screen is refreshed
    if new_car_count == 6:
        car_manager.new_car()
        new_car_count = 0

    # Move the cars
    car_manager.move_cars()

    # Remove cars when they pass the edge of the screen
    car_manager.flush_cars()

    new_car_count += 1

screen.exitonclick()
