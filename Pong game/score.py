from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 200)
        self.write(f"{self.l_score} || {self.r_score}", align='center', font=("Courier", 50, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score} || {self.r_score}", align='center', font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=("Courier", 40, "normal"))
