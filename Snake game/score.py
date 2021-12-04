from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 12, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Data.txt", mode='r') as file:
            self.high_score= int(file.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}    Heighest sccore:{self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def resets(self):
        if self.score > self.high_score:
            self.high_score = self.score

        with open("Data.txt", mode='w') as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
