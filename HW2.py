import turtle
tao=turtle.Pen()
tao.shape('turtle')

def rectangle():
    for i in range(4):
        tao.forward(100)
        tao.left(90)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

def circle(x=30):
    for i in range(x):
        tao.circle(30)
        tao.left(12)
        tao.forward(1)


circle()
Go(-20,20)
circle(60)



    
