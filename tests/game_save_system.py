import json
import random

FILENAME = "game.json"

class Player:
    def __init__(self, name):
         self.name = name
         self.level = 1
         self.experience = 0
         self.health = 100
         self.gold = 100
         self.inventory = []

    def to_dict(self):
         return {
             "name": self.name,
             "level": self.level,
             "experience": self.experience,
             "health": self.health,
             "gold": self.gold,
             "inventory": self.inventory
        }
try:
     with open(FILENAME, "r") as file:
         data = json.load(file)
     player = Player(data["name"])
     player.level = data["level"]
     player.experience = data["experience"]
     player.health = data["health"]
     player.gold = data["gold"]
     player.inventory = data["inventory"]

except FileNotFoundError:
     name = input("enter your name: ")
     player = Player(name)

def save_game():
     with open(FILENAME, "w") as file:
          json.dump(player.to_dict(), file, indent=4)

def expelore():
     xp = random.randint(10, 30)
     gold = random.randint(5, 20)
     player.experience += xp
     player.gold += gold
     print(f"You gained {xp} XP anf found {gold} gold.")
     save_game()

def check_level_up(self):
     while self.experience >= self.level * 100:
          self.level += 1
          self.health = 100
          print(f"Congratulations! Ypu reached level {self.level}!")

def fight():
     enemy_health = random.randint(30, 60)
     player_attack = random.randint(20, 50)
     print(f"Enemy health: {enemy_health}")
     print(f"Your attack: {player_attack}")

     if player_attack >= enemy_health:
         xp = random.randint(20, 40)
         gold = random.randint(10, 30)
         player.experience += xp
         player.gold += gold
         print(f"You won!")
         print(f"You gained {xp} XP and {gold} gold.")
         player.check_level_up
     else:
         damage = random.randint(10, 25)
         player.health -= damage
         print(f"You lost and took {damage} damage.")
         print(f"Your hralth is now {player.health}.")
         save_game()

ITEMS= {
     "sword": 50,
     "shield": 40,
     "potion": 20
}
def buy_item():
     print("\nItems:")
     for item, price in ITEMS.items():
         print(f"{item}: {price} gold")
         item = input("enter item name: ")
     if item not in ITEMS:
             print("Item not found.")
             return

     price = ITEMS[item]
     if player.gold < price:
             print("Not enough gold.")
             return

     player.gold -= price
     player.inventory.append(item)
     print(f"You bought {item}.")
     save_game()

def use_potion():
     if "potion" not in player.inventory:
         print("You don't have a potion.")
         return

     if player.health == 100:
         print("Your health is already full.")
         return

     player.health = min(100, player.health + 30)
     player.inventory.remove("potion")
     print(f"Your health is now {player.health}.")
     save_game

def show_character():
     print("\n---character---")
     print(f"player: {player.name}")
     print(f"level: {player.level}")
     print(f"XP: {player.experience}")
     print(f"health: {player.health}")
     print(f"gold: {player.gold}")
     print(f"inventory:")
     if player.inventory:
         for item in player.inventory:
             print(f" {item}")

     else:
         print(" Emoty")

while True:
     print("1. Expelore\n2. Fight\n3. Buy Item\n4. Use potion\n5. Show character\n6. Exit")
     choice = input("Choose an option: ")
     if choice == "1":
         expelore()

     if choice == "2":
         fight()

     if choice == "3":
         buy_item()

     if choice == "4":
         use_potion()

     if choice == "5":
         show_character()

     if choice == "6":
         save_game()
         print("Game saved. Goodbye!")
         break

     else:
         print("invalid choice")

          
