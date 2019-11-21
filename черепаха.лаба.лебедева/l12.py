def main():
    import turtle

    turtle.shape('turtle')

    turtle.penup()
    turtle.forward(220)
    turtle.pendown()
    turtle.left(90)
    for j in range(1, 4):
        for i in range(1, 61):
            turtle.forward(4)
            turtle.left(360 / 120)
        for i in range(1, 61):
            turtle.forward(1)
            turtle.left(360 / 120)

    turtle.done()


if __name__ == '__main__':
    main()