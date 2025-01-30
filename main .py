from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("Collision with food")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        print("Collision with wall")
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collision with tail
    for seg in snake.turtles[1:]:
        
        if snake.head.distance(seg) < 10:
            print("Collision with tail")
            game_is_on = False
            scoreboard.game_over()

screen.mainloop()








screen.exitonclick()
