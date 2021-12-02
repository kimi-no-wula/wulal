for a in range(100, 1, -1):
    t = 1
    for x in range(100):
        for y in range(100):
            for z in range(100):
                t *= ( (x + 3 * y + 2 * z - 54 != 0) or (a < x + 10) or (a < 5 * y - 4 * x) or (a < z + x) )
    if t == 1:
        print(a)
        break