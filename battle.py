from typing import Union
from player import Player
from enemy import Enemy

def battle(player: Player, opponent: Enemy) -> None:
    
    print("\n===== BATTLE START =====\n")
    
    while player.is_alive() and opponent.is_alive():
        # status display
        player.status()
        opponent.status()
        print()
    
    match player.choose_action():
            case "1":
                player.attack(opponent)
            case "2":
                player.heal(20)
            case _:
                print("Invalid choice — you hesitate and lose the turn.")
