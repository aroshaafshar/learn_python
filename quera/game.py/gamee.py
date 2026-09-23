import random

choices = ["sang", "kaghaz", "gheichi"]

user_score = 0
computer_score = 0

while user_score < 3 and computer_score < 3:

    print("1: sang")
    print("2: kaghaz")
    print("3: gheichi")

    user = input("Entekhab kon: ")

    computer = random.choice(choices)

    if user == "1":
        user = "sang"
    elif user == "2":
        user = "kaghaz"
    elif user == "3":
        user = "gheichi"
    else:
        print("Entekhab eshtebah!")
        continue

    print("Computer entekhab kard:", computer)

    if user == computer:
        print("Mosavi")

    elif user == "sang" and computer == "gheichi":
        print("To bordi")
        user_score += 1

    elif user == "kaghaz" and computer == "sang":
        print("To bordi")
        user_score += 1

    elif user == "gheichi" and computer == "kaghaz":
        print("To bordi")
        user_score += 1

    else:
        print("Computer bord")
        computer_score += 1

    print("Score:", user_score, "-", computer_score)

if user_score == 3:
    print("To barande shodi!")

else:
    print("Computer barande shod!")