from character import Character

class Player(Character):
    def choose_action(self):
        while True:
            print("\nYour Turn! Choose an action:")
            print("1. Attack")
            print("2. Heal")
            choice = input("➤ Enter 1 or 2: ").strip()
            if choice in ["1", "2"]:
                return choice
            else:
                print("❌ Invalid input. Please try again.")