import os

file = open("../../README.md", "w")


def print_file_tree(directory, name, nest=0):
    global file
    if nest > 2:
        file.write("- " * (nest - 1))
    if nest > 1:
        file.write("- ")

    if name == "" and nest == 0:
        file.write("These are my python learning projects" + "\n")
    else:
        file.write("- " + name + "\n")

    for sub_file in os.listdir(directory):
        if sub_file not in (".git", ".idea", "__pycache__"):
            if "." not in sub_file:
                print_file_tree(directory + "\\" + sub_file, sub_file, nest + 1)
            elif sub_file.endswith(".py"):
                if nest > 1:
                    file.write("- " * (nest - 1))
                if nest > 0:
                    file.write("- ")
                file.write("- " + sub_file + "\n")
            else:
                continue


print_file_tree("../../", "")
file.close()
