n = int(input())
for _ in range(n):
    phone = input().strip()
    if    phone.startswith("+98") and len(phone) == 13 and phone[1:].isdigit():
      print(phone)
    elif  phone.startswith("98") and len(phone) == 12 and phone.isdigit():
      print("+" + phone)
    elif  phone.startswith("09") and len(phone) == 11 and phone.isdigit():
      print("+98" + phone[1:])
    else:
      print("invalid")
