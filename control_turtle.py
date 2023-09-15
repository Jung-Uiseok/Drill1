import turtle

def front_move():
    turtle.setheading(90)
    turtle.forward(50)

def back_move():
    turtle.setheading(-90)
    turtle.forward(50)

def left_move():
    turtle.setheading(180)
    turtle.forward(50)
    
def right_move():
    turtle.setheading(0)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.onkey(front_move, 'w')
turtle.onkey(back_move, 's')
turtle.onkey(left_move, 'a')
turtle.onkey(right_move, 'd')
turtle.listen()
