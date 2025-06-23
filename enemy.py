import random
from character import Character

class Enemy(Character):
    
    def decide_action(self) -> str:
        heal_chance = random.random()
        if self.health < self.max_health * 0.35 and heal_chance < 0.6:
            return "heal"
        return "attack"
    
    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        if random.random() < 0.25:
            damage *= 2
            print("💢 Enemy lands a critical hit!")
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage:.0f} damage!")