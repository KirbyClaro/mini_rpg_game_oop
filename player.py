from character import Character

class Player(Character):
    def choose_action(self)->str:
        print("\nChoose an action:")
        print("  1. Attack")
        print("  2. Heal")
        return input("Enter 1 or 2 ➜ ").strip()