# import colorgram
#
# colors = colorgram.extract('image.jpg',20)
# rgb_colors=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

hirst = t.Turtle()
t.colormode(255)
hirst.speed("fastest")
color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10),(243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8),
              (224, 141, 211), (10, 97, 61)]

hirst.penup()
hirst.hideturtle()
hirst.setheading(255)
hirst.forward(300)
hirst.setheading(0)
number_of_dots = 100

for dot_count in range (1, number_of_dots + 1):
    hirst.dot(20, random.choice(color_list))
    hirst.forward(50)

    if dot_count % 10 == 0:
        hirst.setheading(90)
        hirst.forward(50)
        hirst.setheading(180)
        hirst.forward(500)
        hirst.setheading(0)



screen = t.Screen()
screen.exitonclick()
