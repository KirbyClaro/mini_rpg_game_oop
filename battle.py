from player import Player
from enemy import Enemy

def battle(player: Player, opponent: Enemy) -> None:
    
    print("\n===== BATTLE START =====\n")
    
    while player.is_alive() and opponent.is_alive():
        player.status()
        opponent.status()
        print()

        print("---- Player Turn ----")
        match player.choose_action():
            case "1":
                player.attack(opponent)
            case "2":
                player.heal(20)
            case _:
                print("Invalid choice — you hesitate and lose the turn.")

        if opponent.is_alive():
            print("\n---- Enemy Turn ----")
            if opponent.decide_action() == "attack":
                opponent.attack(player)
            else:
                opponent.heal(15)

        print("\n" + "-" * 28 + "\n")

    print("===== BATTLE OVER =====")
    if player.is_alive():
        print("🏆  You are victorious!")
    else:
        print("💀  You were defeated...")

