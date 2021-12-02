x = int(input())
y = int(input())
n = int(input())

max_jump = x + y
print(n // max_jump * 2 + (n - n // max_jump * max_jump) // y + 1)