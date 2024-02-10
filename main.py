from turtle import Turtle, Screen
import random
import turtle

# tommy = Turtle()
# tommy.shape("turtle")
# tommy.color("green")

# tommy.forward(50)
# tommy.right(90)
# tommy.forward(50)


# screen = Screen()

# screen.exitonclick()

tommy = Turtle()

tommy.shape("turtle")

screen = Screen()

# tommy.forward(100)
# tommy.right(120)
# tommy.forward(100)
# tommy.right(120)
# tommy.forward(100)
# tommy.right(120)

# for x in range(0,4):
#   tommy.forward(100)
#   tommy.right(90)

# for x in range(0,10):
#   tommy.forward(20)
#   tommy.penup()
#   tommy.forward(20)
#   tommy.pendown()

# screen.exitonclick()
# # tommy.forward(50)
# # tommy.right(90)
# # tommy.forward(50)

# min_angles = 3
# max_angles = 9

# for x in range(3, max_angles):
#   main_angle = 360
#   angle = main_angle / x
#   print(angle)
#   for _ in range(0,x):
#     tommy.forward(100)
#     tommy.right(angle)

turtle.colormode(255)

lines_count = 50
rotation = [0, 90, 180, 270]
colors = ["green", "red", "blue", "yellow", "orange"]
speed = 0

def random_color():
  r = random.randint(0, 256)
  g = random.randint(0, 256)
  b = random.randint(0, 256)
  color = (r,g,b)
  return color

for x in range(0, lines_count):
  tommy.forward(30)
  tommy.right(random.choice(rotation))
  tommy.pencolor(random_color())
  
  if x <= 7:
    tommy.pensize(x)
  else:
    tommy.pensize(7)
  tommy.speed(speed)
  speed += 1

screen.exitonclick()
