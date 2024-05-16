import turtle
import time

delay = 0.1
score = 0

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#4275f5")
head.up()
head.goto(0, 0)
head.direction = "stop"

segment = turtle.Turtle()
segment.speed(0)
segment.shape("square")
segment.color("white")
segment.penup()
segment.goto(0, 0)
