def main():
    import turtle

    turtle.shape('turtle')

    h = 5
    k = 3 / 120
    m = 120
    for l in range(1, h + 1):
        for d in range(1, m + 1):
            turtle.forward(k * m)
            turtle.left(360 / m)
        turtle.left(360 / h)


    turtle.done()


if __name__ == '__main__':
    main()