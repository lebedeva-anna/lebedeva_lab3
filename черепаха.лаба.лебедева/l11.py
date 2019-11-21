def main():
    import turtle

    turtle.shape('turtle')
    turtle.right(90)
    for k in range(1, 11):
        for i in range(1, 121):
            turtle.forward(3 + k / 2)
            turtle.left(360 / 120)
        turtle.left(180)
        for i in range(1, 121):
            turtle.forward(3 + k / 2)
            turtle.left(360 / 120)




if __name__ == '__main__':
    main()