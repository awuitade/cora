import turtle  

def draw_hello_kitty():  
    turtle.speed(5)  

    # Cabeza  
    turtle.penup()  
    turtle.goto(0, -100)  
    turtle.pendown()  
    turtle.fillcolor("white")  
    turtle.begin_fill()  
    turtle.circle(100)  
    turtle.end_fill()  

    # Ojos  
    turtle.penup()  
    turtle.goto(-40, 20)  
    turtle.pendown()  
    turtle.fillcolor("black")  
    turtle.begin_fill()  
    turtle.circle(10)  
    turtle.end_fill()  

    turtle.penup()  
    turtle.goto(40, 20)  
    turtle.pendown()  
    turtle.begin_fill()  
    turtle.circle(10)  
    turtle.end_fill()  

    # Nariz  
    turtle.penup()  
    turtle.goto(0, 0)  
    turtle.pendown()  
    turtle.fillcolor("pink")  
    turtle.begin_fill()  
    turtle.circle(5)  
    turtle.end_fill()  

    # Bigotes  
    turtle.penup()  
    turtle.goto(-60, -10)  
    turtle.pendown()  
    turtle.goto(-20, -10)  

    turtle.penup()  
    turtle.goto(60, -10)  
    turtle.pendown()  
    turtle.goto(20, -10)  

    # Lazo  
    turtle.penup()  
    turtle.goto(0, 50)  
    turtle.pendown()  
    turtle.fillcolor("red")  
    turtle.begin_fill()  
    turtle.circle(20, 180)  # Lazo izquierdo  
    turtle.left(90)  
    turtle.forward(40)  
    turtle.left(90)  
    turtle.circle(20, 180)  # Lazo derecho  
    turtle.left(90)  
    turtle.forward(40)  
    turtle.end_fill()  

    turtle.hideturtle()  
    turtle.done()  

draw_hello_kitty()