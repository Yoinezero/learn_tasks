def alphabet_position(text):
    return " ".join([str((ord(el) - 64)) for el in text.upper() if el.isalpha()])


print(alphabet_position("The sunset sets at twelve o' clock."))
