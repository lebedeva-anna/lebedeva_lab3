def main():
    import turtle

    turtle.shape('turtle')

    b = 15
    delta = 20
    for j in range(1, 11):
        for i in range(1, 5):
            turtle.forward(b + j * 2 * delta)
            turtle.left(90)
        turtle.penup()
        turtle.right(90)
        turtle.forward(delta)
        turtle.right(90)
        turtle.forward(delta)
        turtle.left(180)
        turtle.pendown()

    turtle.done()


if __name__ == '__main__':
    main()

