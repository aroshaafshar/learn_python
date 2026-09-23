import random

print("bia sang kaghaz gheichi bazi konim")
secret_number = random.choice(["sang", "kaghaz", "gheichi"])
print(["sang", "kaghaz", "gheichi"])
print("1: sang, 2: kaghaz, 3: gheichi")
my_dict = {
"sang": "1",
"kaghaz": "2",
"gheichi": "3" 
}
player1_wins = 0
player2_wins = 0
while player1_wins < 3 and player2_wins < 3:
    secret_number = random.choice([1, 2, 3])
    player1_wins_choice = int(input("enter a number (1, 3): "))
    print(f"Computer choice was: {secret_number}")
    print("eshtebah adad bayad bein 1 ta 3 bashad")
 if secret_number == player1_wins_choice:
    print("mosavi shod")
 elif (player1_wins_choice == 1 and secret_number == 3) or\
     (player1_wins_choice ==2 and secret_number == 1) or\
     (player1_wins_choice ==3 and secret_number == 2):
    print("player 1 wins")
    player1_wins += 1

