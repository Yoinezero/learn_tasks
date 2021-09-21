import os

import student
import students_exceptions


def open_file(n):
    f = None
    try:
        f = open(n, "r")
        if os.stat(n).st_size == 0:
            raise students_exceptions.FileEmpty("File error", n, "File is empty")

    except IOError as ex:
        print("An error occurred: ", os.strerror(ex.errno))
        exit(ex.errno)

    except students_exceptions.FileEmpty as ex:
        print(ex.args[0] + ". " + ex.args[1], " : ", ex.file_name)
        exit(ex.errno)
    return f


name = input("Enter Jekyll's file name: ") + ".txt"
file = open_file(name)
students = {}
count = 0

try:
    for line in file:

        count += 1
        spl = line.rstrip('\n').split()

        if len(spl) != 3:
            raise students_exceptions.BadLine("Line Error", line, f"Bad line at {count} line")

        if not spl[0].isalpha() or not spl[1].isalpha():
            raise students_exceptions.BadLine("Line Error", line, f"Bad line at {count} line")

        try:
            c = float(spl[2])
        except ValueError:
            raise students_exceptions.BadLine("Line Error", line, f"Bad line at {count} line")

        temp = student.Student(spl[0], spl[1])
        if str(temp) in students:
            students[str(temp)] += float(spl[2])
        else:
            students[str(temp)] = float(spl[2])

except students_exceptions.BadLine as e:
    print(e.args[0] + ". " + e.args[1], ": ", e.line)
    exit(e.errno)

for full_name, mark in students.items():
    print(full_name, " ", mark)

file.close()
