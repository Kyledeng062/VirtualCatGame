from cat import Cat

def main():
    print(" Welcome to Virtual Pet Cat! ")
    name = input("Name your pet: ")
    cat = Cat(name)

    while cat.alive:
        cat.display_status()
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Heal")
        print("4. Visit Shop")
        print("5. End Day")
        print("6. Quit")
        choice = input("Choose an action (1-6): ").strip()

        if choice == "1":
            cat.feed()
        elif choice == "2":
            cat.play()
        elif choice == "3":
            cat.heal()
        elif choice == "4":
            cat.visit_shop()
        elif choice == "5":
            cat.end_day()
        elif choice == "6":
            print(f"Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please choose a number between 1 and 6.")

if __name__ == '__main__':
    main()