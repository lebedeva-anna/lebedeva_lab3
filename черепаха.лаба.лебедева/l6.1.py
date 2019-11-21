def main():
    import turtle

    turtle.shape('turtle')

    for m in range(1, 360):
        turtle.forward(m / 50)
        turtle.left(7)

    turtle.done()


if __name__ == '__main__':
    main()