import turtle as t
import math

axiom = "F"
link = {
    "F": "FF-[XY]+[XY]",
    "X": "+FY",
    "Y": "-FX"
}

stack = []
length = 5
alpha = math.pi / 2
theta = math.pi / 8
t.pencolor("black")
t.penup()
t.setpos(0, -270)
t.setheading(90)
t.pendown()
t.speed(0)

for i in range(int(input("Enter count of replacements: "))):
    new_string = ""
    for el in axiom:
        if el in link:
            new_string += link[el]
        else:
            new_string += el
    axiom = new_string

print(axiom)

for el in axiom:
    if el == "F":
        t.forward(length)
    elif el == "[":
        stack.append(length)
        length -= 0.5
        stack.append(t.position())
        stack.append(t.heading())
    elif el == "]":
        t.penup()
        t.setheading(stack.pop())
        t.setposition(stack.pop())
        length = stack.pop()
        t.pendown()
    elif el == "-":
        t.left(math.degrees(theta))
    elif el == "+":
        t.right(math.degrees(theta))
    elif el == "X":
        print("X")
    elif el == "Y":
        print("Y")


t.done()
