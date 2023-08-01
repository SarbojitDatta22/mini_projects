import time

def intro():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself standing in front of a mysterious cave.")
    time.sleep(1)
    print("You don't know what lies inside, but you feel curious.")
    time.sleep(1)
    print("Do you dare to enter the cave?\n")

def choose_path():
    choice = input("Enter '1' to enter the cave or '2' to walk away: ")

    if choice == '1':
        inside_cave()
    elif choice == '2':
        print("\nYou decide not to enter the cave and walk away.")
        print("Thanks for playing!")
    else:
        print("\nInvalid input! Please enter '1' or '2'.")
        choose_path()

def inside_cave():
    print("\nAs you enter the dark cave, you can barely see anything.")
    time.sleep(1)
    print("You hear strange noises echoing through the walls.")
    time.sleep(1)
    print("Suddenly, you spot two glowing eyes in the darkness.")
    time.sleep(1)
    print("A creature approaches you!")
    time.sleep(1)

    choice = input("Will you 'fight' or 'run' away?: ")

    if choice.lower() == 'fight':
        print("\nYou bravely fight the creature.")
        time.sleep(1)
        print("After a fierce battle, you defeat the creature.")
        time.sleep(1)
        print("Congratulations! You have survived the adventure!")
    elif choice.lower() == 'run':
        print("\nYou choose to run away.")
        time.sleep(1)
        print("You escape from the cave and return to safety.")
        time.sleep(1)
        print("Thanks for playing!")
    else:
        print("\nInvalid input! Please enter 'fight' or 'run'.")
        inside_cave()

def main():
    intro()
    choose_path()

if __name__ == "__main__":
    main()
