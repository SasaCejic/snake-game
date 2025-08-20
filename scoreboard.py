from importlib.resources import contents
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score("high_score.txt")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.write_score()

    @staticmethod
    def read_high_score(file_name):
        file = open(file_name)
        content = file.read()
        file.close()
        if content == "":
            return 0
        else:
            return int(content)

    @staticmethod
    def write_high_score(file_name, new_high_score):
        with open(file_name, mode="w") as file:
            file.write(str(new_high_score))

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score("high_score.txt", self.high_score)
        self.score = 0
        self.write_score()