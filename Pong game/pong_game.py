from turtle import Screen
from paddle import Paddle
from ball import Ball
from scory import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(fun=r_paddle.up, key='Up')
screen.onkeypress(fun=l_paddle.up, key='w')
screen.onkeypress(fun=r_paddle.down, key='Down')
screen.onkeypress(fun=l_paddle.down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Detect the collision of ball and the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.reverse()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.reverse()
    ball.move()

    # Detect out of bonds
    if ball.xcor() > 380:
        ball.restore()
        scoreboard.l_point()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.restore()

    if scoreboard.r_score == 5:
        game_is_on = False
        scoreboard.game_over()
    elif scoreboard.l_score == 5:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()

