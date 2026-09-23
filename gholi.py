n = int(input())
for i in range(n, n+1):
    s = " + ".join(str(i) for i in range(1, n+1))
    print(s, " = ", sum(range(1, n+1)))