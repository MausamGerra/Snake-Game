"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html

            if t.xcor() > 200:
                t.goto(-200)
            if t.xcor() < -200:
                t.goto(200)
            if t.ycor() > 200:
                t.goto(-200)
            if t.ycor() < -200:
                t.goto(200)"""

from turtle import Turtle
from turtle import Screen
import random
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

snake=Snake()
scoreboard=Scoreboard()
food=Food()

# Fullscreen the canvas
screen = Screen()
screen.setup(1.0, 1.0)
screen.bgcolor("Black")
screen.title("My Snake Game!")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    elif(snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280):
        game_is_on=False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()
    #if head collides with any segment in the tail:
    #trigger game_over


screen.exitonclick()






