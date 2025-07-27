from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        """Updates the scoreboard for the right and left paddle"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

    def l_point(self):
        """Increases and keeps the score for the left paddle"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increases and keeps the score for the right paddle"""
        self.r_score += 1
        self.update_scoreboard()

