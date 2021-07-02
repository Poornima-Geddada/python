from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

scr = Screen()
scr.setup(600, 600)
scr.title("My Snake Game")
scr.bgcolor("black")
scr.tracer(0)

snake = Snake()
food = Food()
score = Score()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.125)
    snake.move()

    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

scr.exitonclick()
