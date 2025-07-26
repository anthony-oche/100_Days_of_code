from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_UP = 90
MOVE_DOWN = 270
MOVE_RIGHT = 0
MOVE_LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the starting snake body."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        """Creates a segment and adds it to a list."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset_segment(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Adds a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Linked the body of the snake to the head by looping backwards whereby the last segments is taking the
        existing position of the second to last."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Sets the head direction at angle 90"""
        if self.head.heading() != MOVE_DOWN:
            self.head.setheading(MOVE_UP)

    def down(self):
        """Sets the head direction at angle 270"""
        if self.head.heading() != MOVE_UP:
            self.head.setheading(MOVE_DOWN)

    def right(self):
        """Sets the head direction at angle 0"""
        if self.head.heading() != MOVE_LEFT:
            self.head.setheading(MOVE_RIGHT)

    def left(self):
        """Sets the head direction at angle 180"""
        if self.head.heading() != MOVE_RIGHT:
            self.head.setheading(MOVE_LEFT)