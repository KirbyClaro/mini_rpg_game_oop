from player import Player
from enemy import Enemy
from battle import battle

def main() -> None:
    hero   = Player("Hero",   health=100, attack_power=20, defense=5)
    goblin = Enemy ("Goblin", health=80,  attack_power=15, defense=3)
    print("Type of hero:", type(hero))
    print("Does hero have is_alive():", hasattr(hero, "is_alive"))
    battle(hero, goblin)

if __name__ == "__main__":
    main()