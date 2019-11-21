import turtle
turtle.shape('turtle')
k = 1


def circle(m, w, x, y, col):
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.color(col)
    for t in range(1, int(360 / w) + 1):
        turtle.left(w)
        turtle.forward(m * w)
    turtle.end_fill()
    turtle.penup()


def halfcircle(rs):
    for t in range(1, int(360 / 4 / 3) + 1):
        turtle.left(3)
        turtle.forward(rs * k *3)


circle(1 * k, 3, 0, 0, "yellow")
circle(0.18 * k, 3, 23 * k, 75 * k, "blue")
circle(0.18 * k, 3, -27 * k, 75 * k, "blue")
turtle.goto(-1 * k, 60 * k)
turtle.pendown()
turtle.color("black")
turtle.width(7)
turtle.goto(-1 * k, 45 * k)
turtle.penup()
turtle.goto(-37 * k, 35 * k)
turtle.pendown()
turtle.color("red")
turtle.width(10*k)
turtle.right(45)
halfcircle(0.8)

turtle.done()

if __name__ == '__main__':
    main()