def NOT(x):
    return not x


P = [2, 4, 8, 12, 15]
Q = [3, 6, 8, 15]
a = []

for x in range(1, 1000):
    F = ((x in P) <= ((x in Q) or (x in a)))
    if NOT(F):
        a.append(x)

print(sum(a))