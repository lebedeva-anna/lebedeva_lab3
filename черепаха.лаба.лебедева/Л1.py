def main():
    import turtle

    turtle.shape('turtle')

    for i in range(1, 400):
        turtle.forward(i / 50)
        turtle.left(5)

    turtle.done()


if __name__ == '__main__':
    main()







