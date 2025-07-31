import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.make_cars()
    cars.car_movement()
    for car in cars.cars:
        if player.distance(car.position()) < 20:
            game_is_on = False
            score.game_over()
    if player.ycor() > 270:
        player.goto(0, -250)
        score.level_up()
        cars.increase_speed()
    screen.update()

screen.exitonclick()
