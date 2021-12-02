s = int(input())
e = int(input())
n = int(input())
prtl = []
for i in range(n):
    prtl.append(int(input()))


def find_min(s, e, prtl):
    k = 100000000000000000000000000
    kp = 0
    m = 100000000000000000000000000
    mp = 0
    for i in range(len(prtl)):
        if (abs(s - prtl[i])) < k:
            k = abs(s - prtl[i])
            kp = i
        if (abs(e - prtl[i])) < m:
            m = abs(e - prtl[i])
            mp = i
    return k + m + 1


standard = abs(e - s), find_min(s, e, prtl)

print(min(standard))