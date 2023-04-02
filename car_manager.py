from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_turtle = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_turtle(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.shapesize(stretch_len=2)
            new_turtle.penup()
            new_turtle.color(COLORS[random.randint(0, 5)])
            new_turtle.goto(280, random.randint(-250, 250))
            self.all_turtle.append(new_turtle)

    def move(self):
        for cars in self.all_turtle:
            cars.backward(self.speed)

    def inc_speed(self):
        self.speed += MOVE_INCREMENT
