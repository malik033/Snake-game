from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        self.print_initial_positions()  # Print initial positions for debugging

    def create_snake(self):
        for position in starting_position:
            self.add_turtles(position)

    def add_turtles(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.turtles.append(t)

    def extend(self):
        self.add_turtles(self.turtles[-1].position())

    def move(self):
        for turtle_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_num - 1].xcor()
            new_y = self.turtles[turtle_num - 1].ycor()
            self.turtles[turtle_num].goto(new_x, new_y)
        self.turtles[0].forward(move_distance)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def print_initial_positions(self):
        for i, t in enumerate(self.turtles):
            print(f"Segment {i} position: {t.position()}")
