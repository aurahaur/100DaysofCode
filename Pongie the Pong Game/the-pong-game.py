from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoring import Scoring
import time

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pongie the Pong Game")
screen.bgcolor("dark slate gray")
screen.tracer(0)

# Create and move a paddle
pongie_right = Paddle((350, 0))
pongie_left = Paddle((-350, 0))

# Create a ball
ball = Ball()
screen.listen()
screen.onkey(pongie_right.up, "Up")
screen.onkey(pongie_right.down, "Down")
screen.onkey(pongie_left.up, "w")
screen.onkey(pongie_left.down, "s")

# Create scoring
score = Scoring()

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with right or left paddle
    if ball.distance(pongie_right) < 60 and ball.xcor() > 320 \
            or ball.distance(pongie_left) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if ball missed the wall
    if ball.xcor() > 380:
        # Reset the ball's position
        # Left player wins
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        # Reset the ball's position
        # Right player wins
        ball.reset_position()
        score.r_point()
