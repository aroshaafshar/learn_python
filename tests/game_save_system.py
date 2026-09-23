# ============================================================
# PROJECT 6 - GAME SAVE SYSTEM
# ============================================================

"""
Build a small text-based game with a persistent player state.

The player should have at least:

- Name
- Level
- Experience
- Health
- Gold
- Inventory

Example:

    Player: Ali
    Level: 4
    XP: 350
    Health: 80
    Gold: 1,200

    Inventory:
        Sword
        Shield
        Potion

Menu:

1. Explore
2. Fight
3. Buy Item
4. Use Potion
5. Show Character
6. Exit

The exact game rules are up to you.

However, actions should change the player's state.

For example:

- Fighting can increase experience.
- Experience can increase the player's level.
- Fighting can change health.
- Winning can give gold.
- Buying an item decreases gold.
- Using an item changes the player's inventory.
- Using a potion can increase health.

Persistence requirement:

The complete game state must be saved.

Example:

Run #1:

    Level: 3
    Gold: 500
    Health: 80

Close the program.

Run #2:

    Level: 3
    Gold: 500
    Health: 80

The player must continue from the previous state.
"""
