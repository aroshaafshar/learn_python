n = int(input())
sum_div = 0
for i in range(1, n):
    if n % i == 0:
         sum_div = sum_div + i

if sum_div == n:
     print("YES")
else:
     print("NO")