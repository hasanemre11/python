from turtle import Turtle, Screen


class Snake:

    def __init__(self):
        self.segments = []
        self.screen = Screen()
        for pos in [(0, 0), (-20, 0), (-40, 0)]:
            seg = Turtle()
            seg.color("white")
            seg.shape("square")
            seg.penup()
            self.segments.append(seg)
            seg.goto(pos)
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def adding(self):
        seg = Turtle()
        seg.color("white")
        seg.shape("square")
        seg.penup()
        self.segments.append(seg)
        index = self.segments.index(seg)
        seg.goto(self.segments[index - 1].xcor(), self.segments[index - 1].ycor())

    def move(self):
        self.screen.listen()
        self.screen.onkey(self.up, "w")
        self.screen.onkey(self.down, "s")
        self.screen.onkey(self.right, "d")
        self.screen.onkey(self.left, "a")
        for seg in self.segments:
            if self.segments.index(seg) == 0:
                x = seg.xcor()
                y = seg.ycor()
                self.segments[0].forward(20)
            else:
                x1 = seg.xcor()
                y1 = seg.ycor()
                seg.goto(x, y)
                x = x1
                y = y1

    def collision(self):

        if self.segments[0].xcor() > 300 or self.segments[0].xcor() < -300 or self.segments[0].ycor() > 300 or \
                self.segments[0].ycor() < -300:
            return True
        for seg in self.segments[1:]:
            if self.segments[0].distance(seg) < 10:
                return True
