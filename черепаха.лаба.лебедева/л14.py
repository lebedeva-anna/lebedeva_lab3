def main():
    import turtle

    turtle.shape('turtle')

    n = 5
    s =11


    def star(k):
        for i in range(1, k + 1):
            turtle.forward(70)
            turtle.left(180 - 360 / (2 * k))

    turtle.penup()
    turtle.goto(-150, 0)
    turtle.pendown()
    star(n)
    turtle.penup()
    turtle.goto(50,0)
    turtle.pendown()
    star(s)


    turtle.done()


if __name__ == '__main__':
    main()