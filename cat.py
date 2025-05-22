# cat.py
import random

class Cat:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.hunger = 100
        self.happiness = 100
        self.coins = 50
        self.is_sick = False
        self.alive = True
        self.days = 1

    def feed(self):
        if self.is_sick:
            print("Your cat is sick and refuses to eat. Heal it first!")
        elif self.hunger >= 100:
            print("Your cat is already full!")
        else:
            increase = random.randint(10, 20)
            self.hunger = min(100, self.hunger + increase)
            print(f"You fed your cat. Hunger increased by {increase}.")

    def play(self):
        if self.is_sick:
            print("Your cat is sick and doesn't want to play. Heal it first!")
        elif self.happiness >= 100:
            print("Your cat is already very happy!")
        else:
            increase = random.randint(10, 20)
            self.happiness = min(100, self.happiness + increase)
            print(f"You played with your cat. Happiness increased by {increase}.")

    def heal(self):
        if not self.is_sick:
            print("Your cat is not sick.")
        elif self.coins < 20:
            print("Not enough coins to buy medicine.")
        else:
            self.is_sick = False
            self.health = 100
            self.coins -= 20
            print("You healed your cat. Health restored!")

    def end_day(self):
        self.hunger = max(0, self.hunger - random.randint(30, 50))
        self.happiness = max(0, self.happiness - random.randint(30, 50))
        self.coins += 10
        print(f" Day {self.days} completed. You received 10 Cat Coins.")
        self.days += 1

        if self.hunger == 0 or self.happiness == 0:
            if not self.is_sick:
                self.is_sick = True
                self.health = max(0, self.health - 20)
                print("Your cat got sick due to neglect!")

    def visit_shop(self):
        shop_items = {
            "1": {"name": "Ball Toy ", "type": "toy", "effect": 15, "price": 15},
            "2": {"name": "Feather Wand ", "type": "toy", "effect": 25, "price": 25},
            "3": {"name": "Cat Tunnel ", "type": "toy", "effect": 35, "price": 35},
            "4": {"name": "Canned Food ", "type": "food", "effect": 25, "price": 15},
            "5": {"name": "Freeze-Dried Treat ", "type": "food", "effect": 35, "price": 25},
            "6": {"name": "Medicine ", "type": "medicine", "effect": 100, "price": 20},
            "7": {"name": "Exit Shop", "type": "exit", "effect": 0, "price": 0}
        }

        while True:
            print("\n===== Cat Shop  =====")
            for key, item in shop_items.items():
                if item["type"] == "exit":
                    print(f"{key}. {item['name']}")
                elif item["type"] == "medicine" and not self.is_sick:
                    print(f"{key}. {item['name']} - (Unavailable: Your cat is not sick)")
                else:
                    print(f"{key}. {item['name']} - {item['price']} coins")

            choice = input("Select an item to buy (1-7): ").strip()
            if choice not in shop_items:
                print("Invalid choice.")
                continue

            item = shop_items[choice]
            if item["type"] == "exit":
                print("Leaving the shop.")
                break
            if item["type"] == "medicine" and not self.is_sick:
                print("Your cat is not sick. You can't buy medicine now.")
                continue
            if self.coins < item["price"]:
                print("Not enough Cat Coins! ")
                continue

            self.coins -= item["price"]
            if item["type"] == "toy":
                self.happiness = min(100, self.happiness + item["effect"])
                print(f"You bought {item['name']}! Happiness increased by {item['effect']}.")
            elif item["type"] == "food":
                self.hunger = min(100, self.hunger + item["effect"])
                print(f"You bought {item['name']}! Hunger increased by {item['effect']}.")
            elif item["type"] == "medicine":
                self.is_sick = False
                self.health = 100
                print("You bought and used medicine to heal your cat! ")

    def display_status(self):
        print("\n===== Cat Status =====")
        print(f"Name       : {self.name}")
        print(f"Health     : {self.health}%")
        print(f"Hunger     : {self.hunger}%")
        print(f"Happiness  : {self.happiness}%")
        print(f"Coins      : {self.coins} ")
        print(f"Is Sick?   : {'Yes' if self.is_sick else 'No'}")
        print(f"Day        : {self.days}")
        print("==========================")