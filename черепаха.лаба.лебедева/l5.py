def main():
    import turtle

    turtle.shape('turtle')

    m = 20
    k = 60

    for l in range(1, m + 1):
        turtle.forward(k)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(k)
        turtle.left(180)
        turtle.left((360 / m))

    turtle.done()


if __name__ == '__main__':
    main()













