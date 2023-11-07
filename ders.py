import stdarray
import stdio

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]


n = len(a)
m = len(b[0])
c = stdarray.create2D(n, m, 0.0)
for i in range(n):
    for j in range(m):
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]
for row in c:
    stdio.writeln(row)
