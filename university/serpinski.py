from turtle import *
import math


def triangle(x1, x2, x3, y1, y2, y3):
    begin_fill()
    penup()
    setposition(x1, y1)
    pendown()
    setposition(x2, y2)
    setposition(x3, y3)
    setposition(x1, y1)
    end_fill()


def draw_triangle(x1, y1, x2, y2, x3, y3, depth):

    color("black", "white")

    x1n = (x1 + x2) / 2
    y1n = (y1 + y2) / 2
    x2n = (x2 + x3) / 2
    y2n = (y2 + y3) / 2
    x3n = (x1 + x3) / 2
    y3n = (y1 + y3) / 2

    triangle(x1n, x2n, x3n, y1n, y2n, y3n)

    if depth > 1:
        depth -= 1
        draw_triangle(x1, y1, x1n, y1n, x3n, y3n, depth)
        draw_triangle(x1n, y1n, x2, y2, x2n, y2n, depth)
        draw_triangle(x3n, y3n, x2n, y2n, x3, y3, depth)


def main():
    n = int(input("Enter a depth of the triangle: "))
    hideturtle()
    speed(0)
    color("black", "blue")
    Xa = 0
    Ya = 180
    Xb = -150 * math.sqrt(2)
    Yb = -30
    Xc = -Xb
    Yc = Yb
    k = 1.5
    triangle(k*Xa, k*Xb, k*Xc, k*Ya, k*Yb, k*Yc)
    draw_triangle(k*Xa, k*Ya, k*Xb, k*Yb, k*Xc, k*Yc, n)

    done()


if __name__ == "__main__":
    main()
