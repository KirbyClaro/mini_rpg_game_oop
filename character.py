import random

class Character:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        
    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        if random.random() < 0.2:
            damage *= 2
            print("⚡ Critical hit!")
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage:.0f} damage!")
        
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        
    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} heals for {amount} HP!")