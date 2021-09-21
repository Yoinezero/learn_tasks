def decrypt(text, n):
    if n <= 0: return text
    ch = list(text)
    m = len(text)//2
    for i in range(n):
        ch[1::2], ch[::2] = ch[:m], ch[m:]
    return "".join(ch)


def encrypt(text, n):
    if n <= 0: return text
    temp = text[:]
    for i in range(n):
        temp = temp[1::2] + temp[::2]
    return temp
