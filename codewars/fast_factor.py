def list_squared(m, n):
    #result = [[1, 1]] if m == 1 else []
    result = []
    for num in range(m, n):
        divs = {1, num ** 2}
        for probe in range(2, int(num ** 0.5) + 1):
            if num % probe == 0:
                divs.add(probe ** 2)
                divs.add(int(num / probe) ** 2)
        if pow(sum(divs), 0.5).is_integer():
            result.append([num, sum(divs)])

    return result
