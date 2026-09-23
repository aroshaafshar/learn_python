n = int(input())

total = 0

def calculation(c, f):
    return c * f


for line in range(n):
    count, fee = input().split()
    total += int(count) * int(fee)
    # total += calculation(int(count), int(fee))

print(total)