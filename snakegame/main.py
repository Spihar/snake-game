from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
import music

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("snake game")

#music included

music.play()
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_on = True


while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.update()
        snake.extend()

    if snake.segments[0].xcor() >= 300 or snake.segments[0].xcor() <= -300 or snake.segments[0].ycor() >= 300 or \
            snake.segments[0].ycor() <= -300:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments:
        if snake.segments[0] == segment:
            continue
        elif snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
