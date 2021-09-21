from turtle import *

def branch(angle, length):
    if length > 1:
        right(angle)
        forward(length*0.67)
        branch(angle, length*0.67)
        backward(length*0.67)
        left(2*angle)
        forward(length * 0.67)
        branch(angle, length * 0.67)
        backward(length * 0.67)
        right(angle)

def main():
    speed(0)
    hideturtle()

    color('blue', 'yellow')
    left(90)
    tracer(0, 0)
    for i in range(360):
        penup()
        goto(0, -300)
        pendown()
        clear()

        length = 150
        forward(length)
        branch(i, length)
        update()
    done()


if __name__ == '__main__':
    main()
