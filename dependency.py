import turtle


def draw_square(square):
    for i in range(0, 2):
        square.forward(100)
        square.right(30)
        square.forward(100)
        square.right(150)


def draw_flower():

    tl = turtle.Turtle()
    screen = turtle.Screen()
    tl.shape("turtle")
    tl.color("pink")
    screen.setup(1000, 1000)

    for i in range(0, 36):
        draw_square(tl)
        tl.speed(8)
        tl.right(10)

    for i in range(0, 4):
        tl.circle(50)
        tl.speed(8)
        tl.right(90)

    tl.speed(8)
    tl.right(90)

    tl.color("green")
    tl.speed(8)
    tl.forward(300)
    tl.speed(8)
    tl.right(90)

    draw_square(tl)
    tl.speed(8)
    tl.left(180)

    draw_square(tl)
    tl.speed(8)
    tl.left(270)
    tl.speed(8)
    tl.forward(200)
    turtle.done()
