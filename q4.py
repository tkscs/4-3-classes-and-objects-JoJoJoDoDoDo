import turtle
import random
turtle.dot()
class Point:
    """a point"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"point A is at ({self.x}), ({self.y})"
    def draw(self):
        turtle.penup()
        turtle.goto (self.x, self.y)
        turtle.dot(500)
    

        


point1 = Point(0,0)
point2 = Point(100,0)
point3 = Point(100,100)
point4 = Point(0, 100)

point1.draw()
point2.draw()
point3.draw()
point4.draw()



turtle.exitonclick()