import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(tim.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    if tim.is_at_finishline():
        score.level_increment()
        car.increase_speed()

    for _ in car.all_cars:
        if _.distance(tim) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()

