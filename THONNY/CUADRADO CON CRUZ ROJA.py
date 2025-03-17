#FANNY MAZ Y SAHILY LUNA
#cuadrado azul con una cruz roja
  
  
import turtle 
turtle.speed(9)
def dibujar_cuadro():
    turtle.pencolor("blue")
    turtle.penup()
    turtle.goto(-100,100)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
       
dibujar_cuadro()

def dibujar_rectángulo():
   
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    
    turtle.penup()
    turtle.goto(-10,-200)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(115)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(115)
    turtle.end_fill()
          
dibujar_rectángulo()

def dibujar_rectángulo():
    
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    
    turtle.penup()
    turtle.goto(200,-100)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(115)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(115)
    turtle.end_fill()
    
dibujar_rectángulo()
    
    

    