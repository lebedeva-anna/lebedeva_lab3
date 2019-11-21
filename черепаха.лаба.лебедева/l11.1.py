def main():
    import turtle
    import math

    turtle.shape('turtle')

    k = 3
    m = 10
    b = 20
    l = 50
    turtle.penup()
    for j in range(k, m + 1):
        turtle.forward(l)
        a = 2 * (l + 20) * math.sin(math.pi / j)
        turtle.pendown()
        turtle.left(90 + 180 / j)
        for i in range(1, j + 1):
            turtle.forward(a)
            turtle.left(360 / j)
        turtle.right(90 + 180 / j)
        turtle.penup()
        R = (l + 20) / (math.cos(math.pi / j / 2))
        turtle.goto(0, 0)
        l = R

    turtle.done()


if __name__ == '__main__':
    main()