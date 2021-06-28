
import turtle




def tegn(længde, vinkel, gentagelser, forøgelse=0):
   tegn = turtle.Turtle()
   tegn.speed(0)
   for antal in range(0, gentagelser):
            længde += forøgelse
            tegn.forward(længde)
            tegn.lt(vinkel)
         
   turtle.exitonclick()