import turtle   # import turtle as t, import turtle *

def up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def down():
     turtle.setheading(270)
     turtle.forward(50)
     turtle.stamp()

def left():
     turtle.setheading(180)
     turtle.forward(50)
     turtle.stamp()

def right():
     turtle.setheading(0)
     turtle.forward(50)
     turtle.stamp()

def clear():
    turtle.reset()  #   clear() : 화면만 초기화, home() : 위치만 초기화

turtle.shape("turtle")
turtle.onkeypress(up,"W")
turtle.onkeypress(up,"w")
turtle.onkeypress(down,"S")
turtle.onkeypress(down,"s")
turtle.onkeypress(left,"A")
turtle.onkeypress(left,"a")
turtle.onkeypress(right,"D")
turtle.onkeypress(right,"d")
turtle.onkeypress(clear, "Escape")
turtle.listen()
