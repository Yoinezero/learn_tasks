def tests(exercise, expectation):
    if caesar(exercise) == expectation:
        return "200 OK"
    return "404 ERROR"


def move(char, roll=1):
    return ord(char) + roll - (26 if ord(char.lower()) + roll > ord("z") else 0)


def caesar(ex):
    decrypted = ""
    for sym in ex[0]:
        if not sym.isalpha():
            decrypted += sym
        else:
            decrypted += chr(move(sym, ex[1]))
    return decrypted


print(tests(("abcxyzABCxyz 123", 2), "cdezabCDEzab 123"))
print(tests(("The die is cast", 25), "Sgd chd hr bzrs"))
