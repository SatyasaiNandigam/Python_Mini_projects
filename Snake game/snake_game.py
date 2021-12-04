from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("MY SNAKE GAME")
screen.tracer(0)
user_level= screen.textinput(title='Enter your difficulty', prompt='Which difficulty you choose? Easy/Medium/Hard')
print(f"You selected {user_level}.")

game_is_on = True
snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_is_on:
    screen.update()
    if user_level == 'easy':
        time.sleep(0.15)
    elif user_level == 'medium':
        time.sleep(0.08)
    else:
        time.sleep(0.05)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreBoard.increase_score()
        food.refresh()
        snake.extend()

    # Detect the collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreBoard.resets()
        snake.resets()

    # Detect the collision with tails
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreBoard.resets()
            snake.resets()


screen.exitonclick()
