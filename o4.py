N = int(input())
D = int(input())
An = []
for i in range(N):
    An.append(int(input()))

def way(srt):
    global D, An
    lian = An[srt] // D
    return lian + srt

out = [0]
for j in range(N):
    if j <= max(out):
        out.append(way(j))
print(max(out) + 1)