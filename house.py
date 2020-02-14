#Luis Machuca
#02/14/2020
#this program will have a green background,have a white square,and a red triangle.
import turtle
turtle.Screen().bgcolor("green")
house = turtle.Turtle()
t = turtle.Turtle()

# Make a square
house.pen("blue")
house.fillcolor("white")
house.begin_fill()
house.forward(200)
house.right(90)
house.forward(200)
house.right(90)
house.forward(200)
house.right(90)
house.forward(200)
house.end_fill()
# Position for roof
house.right(180)

# Position for roof
house.left(90) #paired

# Make a roof
house.pen("red")
house.fillcolor("red")
house.begin_fill()
house.forward(200)
house.right(-120)
house.forward(200)
house.right(-120)
house.forward(200)
house.right(-120)
house.end_fill()

