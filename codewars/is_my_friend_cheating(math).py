def remov_nb(n):
    s = n * (n + 1) / 2
    res = []
    for a in range(1, n + 1):
        b = (s - a) / (a + 1)
        if n >= b == int(b):
            res.append((int(a), int(b)))
    return sorted(res, key=lambda x: x[0])