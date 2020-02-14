#Luis Machuca
#02/13/2020

#this program draws a polygon 
sides = int(input ("enter number of sides in a polygon?" ))
lenght = int(input ("enter the length of the side?" ))
linecolor = input ("what color will you like to have for the regular polygon?" )
fillcolor = input ("What is fill color of a regular polygon?" )

angle = (360/sides)
import turtle
t= turtle.Turtle()
turtle.Screen().bgcolor("yellow")
t.color(linecolor)
t.begin_fill()
for f in range (sides):
    t.forward(lenght)
    t.right(angle)
t.fillcolor(fillcolor)
t.end_fill()

