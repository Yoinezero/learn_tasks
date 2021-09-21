from turtle import *
import math


def line(x1, x2, y1, y2):
    penup()
    setposition(x1, y1)
    pendown()
    setposition(x2, y2)


def koch(x1, x2, y1, y2, n):
    if n > 0:
        dx = (x2 - x1) / 3  # math.fabs
        dy = (y2 - y1) / 3  # math.fabs

        x1n = x1 + dx
        y1n = y1 + dy

        x2n = x1 + 2 * dx
        y2n = y1 + 2 * dy

        x_mid = dx / 2 - dy * math.sin(math.pi / 6) + x1n
        y_mid = dy / 2 + dx * math.sin(math.pi / 6) + y1n

        koch(x1, x1n, y1, y1n, n - 1)
        koch(x1n, x_mid, y1n, y_mid, n - 1)
        koch(x_mid, x2n, y_mid, y2n, n - 1)
        koch(x2n, x2, y2n, y2, n - 1)
    else:
        line(x1, x2, y1, y2)


def main():
    n = int(input("Enter a depth of snowflake: "))
    hideturtle()
    speed(0)
    pencolor("black")
    begin_fill()
    corners = 300
    level = 0

    line(-corners, corners, level, level)
    clear()
    koch(-corners, corners, level, level, n)

    end_fill()
    done()


if __name__ == '__main__':
    main()
