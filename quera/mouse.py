x1, x2 = map(int, input().split())
if x1 == x2:
   print("saal noo mobarak!")
else:
   if x2 > x1:
      print("R" * (x2 - x1))
   else:
      print("L" * (x1 - x2))
