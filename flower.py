from turtle import *


def drawPetal(turtle, width):
    """
    Write a function to draw the petal shape for the flower head.  It
    can be a square, triangle, etc.  
    """
    for x in range(4):
        turtle.forward(width)
        turtle.left(90)
    pass


def drawHead(turtle,xpos,ypos):
    """
    Write a function to draw a spirograph like pattern as the flower head.
    It should call drawPetal in a loop and turn after each call to form a circle

    :param turtle: An instance of the Turtle class
    """
    turtle.penup()
    turtle.goto(xpos,ypos)
    turtle.pendown()
    turtle.color("black")
    for x in range(12):
        drawPetal(turtle,30)
        turtle.left(30)
    pass
    


def drawStem(turtle, xpos, ypos, width, length,color):
    """
    Write a function to draw a stem on the screen using the specified parameters.

    :param turtle: An instance of the Turtle class
    :param xpos: The X-axis coordinate for the starting point of the Stem
    :param ypos: The Y-axis coordinate for the starting point of the Stem
    :param width: The width of a side of the Stem
    :param length: The length of a side of the Stem
    :param color: The line color and fill color to use for the Stem
    """
    turtle.penup()
    turtle.goto(xpos,ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
    turtle.end_fill()
    pass



def draw_flower(turtle,xpos,ypos):
    """
    Write a function to draw a flower.  Draw the head and stem.

    :param turtle: the turtle to draw with
    """
    drawHead(turtle,xpos,ypos)
    drawStem(turtle,(xpos-10),(ypos-30),20,65,"brown")
    pass

def main():
    """
    Write a function that will be called when you run this program
    from the terminal.

    Make sure to create a Screen object, a Turtle object,
    and call draw_flower. 

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting untill you close the drawing window.
    """
    space = Screen()
    eddie = Turtle()
    draw_flower(eddie,0,0)
    draw_flower(eddie,-100,0)
    draw_flower(eddie,100,0)
    space.exitonclick()
    pass


# Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()


