#FANNY MAZ Y SAHILY LUNA
import turtle 
turtle.speed(9)

def dibujar_planetatierra():
    turtle.pencolor("blue")
    turtle.penup()
    turtle.goto(-222,-220)
    turtle.pendown()
    r=20
    turtle.circle(r)
    
dibujar_planetatierra()

def dibujar_trayectoia():
    turtle.pencolor("blue")
    turtle.penup()
    turtle.goto(-200,-200)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.penup()
    turtle.pendown()
    turtle.pencolor("magenta")
    turtle.forward(35)
    turtle.left(90)
    turtle.penup()
    turtle.pendown()
    turtle.pencolor("green")
    turtle.forward(45)
    turtle.right(90)
    turtle.penup()
    turtle.pendown()
    turtle.pencolor("yellow")
    turtle.forward(52)
    turtle.right(90)
    turtle.penup()
    turtle.pendown()
    turtle.pencolor("orange")
    turtle.forward(85)
    turtle.left(90)
    turtle.penup()
    turtle.pendown()
    turtle.pencolor("black")
    turtle.forward(55)
    turtle.left(90)
    turtle.penup()
    turtle.pendown()
    turtle.pencolor("red")
    turtle.forward(47)
    turtle.right(90)
    turtle.penup()
    turtle.pendown()
    turtle.pencolor("purple")
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()
    turtle.pendown()
    turtle.pencolor("brown")
    turtle.forward(35)
    
    
dibujar_trayectoia()

def dibujar_planetamarte():
    turtle.pencolor("red")
    turtle.penup()
    turtle.goto(20,-100)
    turtle.pendown()
    r=40
    turtle.circle(r)
    
dibujar_planetamarte()