from player import Player
from enemy import Enemy
from battle import battle

def main() -> None:
    hero   = Player("Hero",   health=100, attack_power=20, defense=5)
    goblin = Enemy ("Goblin", health=80,  attack_power=15, defense=3)
    battle(hero, goblin)

if __name__ == "__main__":
    main()