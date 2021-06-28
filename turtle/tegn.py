
import turtle


figur = turtle.Turtle()

def tegnefigur(længde, vinkel, gentagelser):
    for antal in range(0, gentagelser):
            figur.forward(længde)
            figur.lt(vinkel)
            turtle.exitonclick

