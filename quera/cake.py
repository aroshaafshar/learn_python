n = int(input())
found = False
for a in [1, 2, 3]:
    for b in [1, 2, 3]:
        for c in [1, 2, 3]:
            total = a + b + c
            if total % n == 0:
                found = True
if found:
    print("YES")
else:
    print("NO")