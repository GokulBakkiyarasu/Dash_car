import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=turtle.move_forward)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_turtle()
    for cars in car.all_turtle:
        if turtle.distance(cars) < 25:
            scoreboard.game_over()
            game_is_on = False
    if turtle.ycor() == 280:
        turtle.goto(0, -280)
        scoreboard.inc_score()
        car.inc_speed()
    car.move()

screen.exitonclick()
