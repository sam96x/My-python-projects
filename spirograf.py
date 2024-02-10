from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

tommy = Turtle()

tommy.shape("turtle")

screen = Screen()

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color = (r,g,b)
  return color

circle_angle = 360
c

for number in range(18):
  tommy.pencolor(random_color())
  tommy.circle(80)
  tommy.left(20)


screen.exitonclick()
