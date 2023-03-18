from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.color("black")
        self.level = 1
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_increment(self):
        self.level += 1
        self.clear()
        self.update_level()

    def level_reset(self):
        self.level = 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=FONT)

