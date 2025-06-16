import random

class Character:
    def __init__(self, name: str, health: int, attack_power: int, defense: int):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.defense = defense