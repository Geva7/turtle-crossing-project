from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.cars = []
        self.hideturtle()
        # self.make_cars()
        self.starting_move_speed = 5

    def make_cars(self):
        random_chance = random.randint(1, 5)
        if random_chance == 5:
            random_color = random.choice(COLORS)
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random_color)
            random_y = random.randint(-200, 200)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def car_movement(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(self.starting_move_speed)

    def rotation(self):
        for car in self.cars:
            if car.xcor() == 300:
                car.goto = (300, car.ycor())

    def increase_speed(self):

        self.starting_move_speed += 2



