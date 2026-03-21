from string import ascii_letters

alfa = ascii_letters
delta = int(input())


def code(line):
    res = ''
    for ch in line:
        if ch in alfa:
            res += alfa[alfa.index(ch) - delta]
        else:
            res += ch
    return res

def decode(line):
    res = ''
    for ch in line:
        if ch in alfa:
            res += alfa[alfa.index(ch) - len(alfa) + delta]
        else:
            res += ch
    return res

line = 'Stankovskiy'
codeed = code(line)
decoded = decode(codeed)
print(codeed)
print(decoded)



