N = int(input())
K = int(input())
if N == K:
    print(0)
else:
    print(int(((((N ** 2) / K ** 2) ** 0.5) - 1) * (((N ** 2) / K ** 2) ** 0.5) * 2 * K))