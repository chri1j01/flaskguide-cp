
import turtle


figur = turtle.Turtle()

def tegn(længde, vinkel, gentagelser):
    for antal in range(0, gentagelser):
            figur.forward(længde)
            figur.lt(vinkel)


#trekant
#tegn(200, 360/3, 3)
#firkant
#tegn(100, 360/4, 4)
#ottekant
#tegn(100, 360/8, 8)
#stjerne
#tegn(100, 135, 8)
tegn(50, 91, 100000)


turtle.exitonclick()