from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.position_to_follow = (0,0)
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.setpos(position)
        self.segments.append(segment)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.position_to_follow = (0, 0)
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self, screen):
        for i in range(len(self.segments)):
            if i == 0:
                self.position_to_follow = self.segments[i].position()
                self.segments[i].forward(MOVE_DISTANCE)
            elif i < len(self.segments) -1:
                initial_position = self.segments[i].position()
                self.segments[i].goto(self.position_to_follow)
                self.position_to_follow = initial_position
            else:
                self.segments[i].goto(self.position_to_follow)

        screen.update()
        time.sleep(0.1)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.segments[0].setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
