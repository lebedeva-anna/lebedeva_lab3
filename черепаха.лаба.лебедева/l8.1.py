def main():
    import turtle

    turtle.shape('turtle')

    for j in range(31):
        turtle.forward(50 + 5 * j)
        turtle.left(90)

    turtle.done()


if __name__ == '__main__':
    main()