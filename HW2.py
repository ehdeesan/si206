# Your name: Edison Chiu
# Your student id: 52872908
# Your email: edisonc@umich.edu
# List who you worked with on this homework:

# import the turtle functions for use in this program
# don't need to use the module name
from turtle import *


def draw_circle(turtle, xpos, ypos, radius, color):
    """
    :param turtle: An instance of the Turtle class
    :param xpos: The X-axis coordinate for the starting point of the circle
    :param ypos: The Y-axis coordinate for the starting point of the circle
    :param radius: The radius of the circle
    :param color: The line color and fill color to use for the circle
    """
    turtle.goto(xpos, ypos)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    pass


def draw_rectangle(turtle, xpos, ypos, width, height, color):
    turtle.penup()
    turtle.color(color)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    """
    :param turtle: An instance of the Turtle class
    :param xpos: The X-axis coordinate for the starting point of the shape
    :param ypos: The Y-axis coordinate for the starting point of the shape
    :param width: The width of the shape
    :param height: The height of the shape
    :param color: The line color and fill color to use for the shape
    """
    pass


def draw_rhombus(turtle, xpos, ypos, angle_a, side_length, color):
    turtle.penup()
    turtle.color(color)
    turtle.goto(xpos, ypos)
    turtle.pendown()    
    turtle.begin_fill()
    angle_b = 180 - angle_a
    for x in range(2):
        turtle.left(angle_b / 2)
        turtle.forward(side_length)
        turtle.left(angle_a)
        turtle.forward(side_length)
        turtle.left(angle_b / 2)
    turtle.end_fill()
    """
    :param turtle: An instance of the Turtle class
    :param xpos: The X-axis coordinate for the starting point of the shape
    :param ypos: The Y-axis coordinate for the starting point of the shape
    :param angle_a: One angle of the shape in degrees
    :param side_length: The side length of the shape
    :param color: The line color and fill color to use for the shape
    """
    pass

def draw_e(turtle, xpos, ypos, height):
    turtle.width(8)
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pencolor('black')
    turtle.pendown()
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(height / 3)
    turtle.penup()
    turtle.goto(xpos, ypos + height / 2)
    turtle.pendown()
    turtle.forward(height / 3)
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.forward(height / 3)

def draw_c(turtle, xpos, ypos, height):
    turtle.penup()
    turtle.goto(xpos + 100, ypos)
    turtle.pendown()
    turtle.forward(height / 2)
    turtle.penup()
    turtle.goto(xpos + 100, ypos)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(height / 2)

def draw_initials(turtle, xpos, ypos, height):
    draw_e(turtle,xpos, ypos, height)
    draw_c(turtle,xpos, ypos, height)


def draw_triangle(turtle, xpos, ypos, side_length, color):
    turtle.penup()
    turtle.color(color)
    turtle.goto(xpos, ypos)
    turtle.pendown()    
    turtle.begin_fill()
    for x in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()
# Feel free to create other shapes using more functions like draw_SHAPE3, draw_SHAPE4, etc.


def draw_globe(turtle):
    draw_circle(turtle, 0, 0, 150, '#d3d3d3')
    draw_rectangle(turtle, -10, 20, 20, 65, 'brown')
    draw_rhombus(turtle, 0, 150, 45, 65, 'green')
    draw_rhombus(turtle, 0, 100, 45, 65, 'green')
    draw_rhombus(turtle, 0, 60, 45, 65, 'green')
    draw_rectangle(turtle, -150, -35, 300, 35, 'black')
    draw_triangle(turtle, -50, 250, 10, 'white')
    draw_triangle(turtle, -35, 175, 10, 'white')
    draw_triangle(turtle, 60, 200, 10, 'white')
    draw_triangle(turtle, 20, 130, 10, 'white')
    draw_triangle(turtle, -30, 65, 10, 'white')
    draw_triangle(turtle, -95, 90, 10, 'white')
    draw_triangle(turtle, 100, 115, 10, 'white')
    draw_initials(turtle, -80, -250, 120)
    """
    Write a function to create a snow globe and tree by calling draw_circle,
    draw_SHAPE, draw_SHAPE2 and any other functions (at least once each).

    Feel free to modify the arguments of this function as you like,
    but you should pass in the turtle object at the very least.

    Extra credit for using additional functions to add accessories to the snow globe
    like a base or snow or any other additional object in the snow globe. You can also earn extra credit for signing your
    art with your initials in block letters.
    """

    pass



def main():
    space = Screen()
    eddie = Turtle()
    draw_globe(eddie)
    space.exitonclick()
    """
    Write a function that will be called when you run this program
    from the terminal.

    Make sure to create a Screen object, a Turtle object,
    and call draw_globe.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting untill you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color. You can also call the .color() method on your Turtle
    instance if you want to change its color.
    """

    pass


# Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()
