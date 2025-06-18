import random
from character import Character

class Enemy(Character):
    
    def decide_action(self) -> str:
        low_hp = self.health <= 0.25 * self.max_health
        return "heal" if low_hp and random.random() < 0.5 else "attack"