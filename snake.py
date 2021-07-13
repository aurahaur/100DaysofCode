from turtle import Turtle

positions = [(20, 0), (0, 0), (-20, 0)]

move_distance = 20

up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for i in positions:
            self.add_snake(i)

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def add_snake(self, position):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.color("chartreuse4")
        new_snake.setpos(position)
        self.snakes.append(new_snake)

    def extend(self):
        post = self.snakes[-1].position()
        self.add_snake(post)
