import random

class Character:
    def __init__(self, name: str, health: int, attack_power: int, defense: int):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        
    def attack(self, target: "Character") -> None:
        """Deal damage to a target, with a 20 % crit chance."""
        damage = max(0, self.attack_power - target.defense)
        if random.random() < 0.20:   # crit!
            damage *= 2
            print("⚡  Critical hit!")
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage:.0f} damage.")
        
    def take_damage(self, amount: int) -> None:
        self.health = max(self.health - amount, 0)