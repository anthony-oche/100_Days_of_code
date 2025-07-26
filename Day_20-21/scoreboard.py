from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial", 15, "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Handles the updating of the scoreboard"""
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        """Increases the score everytime the snakes comes in contact with the food and update the scoreboard"""
        self.score += 1
        self.update_scoreboard()

    def reset_game(self):
        """Resets the score to zero everytime the snake dies"""
        if self.score > self.highscore:
            self.highscore = self.score
        with open('data.txt', mode="w") as data:
            data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

