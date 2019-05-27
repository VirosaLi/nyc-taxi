
def baseN(num, b, numerals="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


numerals="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base_n(num, b):
    return ((num == 0) and numerals[0]) or (base_n(num // b, b).lstrip(numerals[0]) + numerals[num % b])


print(baseN(5445, 26))
print(base_n(5445, 26))

