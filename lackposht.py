from turtle import * 


circle_size = input("please enter your circle's size: ")
circle_size = int(circle_size)

circle_color = input("what's color do you want?: ")

circle_width = input("what's width do you want?: ")
circle_width = int(circle_width)

pencolor(circle_color)
pensize(circle_width)
circle(circle_size)