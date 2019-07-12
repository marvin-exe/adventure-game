import time
import random


def print_pause(msg):
    print(msg)
    time.sleep(1)


inventory = []
weapons = ["Virtuous Contract", "Cruel Oath", "Angel's Folly", "Beastlord"]
bosses = ["Alien Leader", "Machine Songstress", "Alien Overlord",
          "Soul Trader"]
boss = random.choice(bosses)
sword = random.choice(weapons)
factory_boss = random.choice(bosses)


def intro():
    print_pause("Distant Future")
    print_pause("Aliens have invaded and humanity"
                " has fled to the moon to survive")
    print_pause("You are an android created by humans"
                " to reclaim Earth from the aliens")
    print_pause("On your way down to Earth your ship is shot down,"
                " you eject and land in an open area")
    print_pause("In front of you is a tower which seems to be protected"
                " by some kind of firewall")
    print_pause("To your left you see an alien patrol")
    print_pause("To your right you hear something, some kind of wierd singing")
    print_pause("Behind you you see smoke which seems to come"
                " from your crashed ship\n")


def game_start():
    print_pause("What do you want to do?")
    print("1. Go to tower\n"
          "2. Approach alien patrol\n"
          "3. Follow the singing\n"
          "4. Go to your ship\n")
    while True:
        choice = input("(Please enter the number of your choice)\n")

        if choice == "1":
            tower_entrance()

        elif choice == "2":
            patrol()

        elif choice == "3":
            singing()

        elif choice == "4":
            ship()


def tower_entrance():
    if "code" in inventory:
        print_pause("As you approach the tower you hear a voice,"
                    " it says 'Code verified, access granted'\n"
                    "The tower door opens and you go inside")
        inside_tower()
    else:
        print_pause("You find yourself in the entrance of the tower,"
                    " you can't go in\n"
                    "You seem to be missing some type of code to be able to "
                    "enter the tower")
        game_start()


def inside_tower():
    print_pause("You are inside and the only thing you can see"
                " is a staircase that goes up")
    print_pause("As you make your way up you find a big empty room")
    print_pause("From the ground you see a platform open up")
    print_pause("The "+boss+" appears and tries to attack you")
    print_pause("What will you do?")
    print("1. Attack\n"
          "2. Run Away\n")
    while True:
        combat_choice = input("Enter 1 or 2\n")
        if combat_choice == "1":
            print_pause("You attack the " + boss + " with your sword,"
                        " it's a critical hit")
            print_pause("The " + boss + " falls down and you see the remaining"
                        " alien forces retreating.")
            print_pause("You are victorious")
            play_again()
        elif combat_choice == "2":
            print_pause("You run away safely")
            game_start()


def patrol():
    if "code" in inventory:
        print_pause("You see only the remains of the patrol")
        print_pause("There's nothing else to do so you go back")
        game_start()
    else:
        print_pause("You approach the patrol carefully")
        while True:
            print("What do you want to do?\n"
                  "1. Attack\n"
                  "2. Go away\n")

            attack_choice = input("Enter 1 or 2\n")

            if attack_choice == "1":
                if "sword" in inventory:
                    print_pause("You attack the patrol with your sword"
                                " and kill the aliens")
                    print_pause("From one of the aliens you take a code chip")
                    inventory.append("code")
                    game_start()
                else:
                    print_pause("You attack the patrol without a weapon")
                    print_pause("The patrol shoots you down")
                    print_pause("You died")
                    play_again()
            elif attack_choice == "2":
                print_pause("You back off before the patrol notices you")
                game_start()


def singing():
    if "joke" in inventory:
        print_pause("The machine continues humming without a care in"
                    " the world")
        print_pause("You go back")
        game_start()
    else:
        print_pause("You follow the wierd voice,"
                    " it seems to be coming from a machine")
        print_pause("It doesn't seem to be hostile so you go near it")
        print_pause("As you approach, the machine notices and greets you")
        print_pause("The machine asks if you want to hear a joke")
        while True:
            hear_joke = input("Hear the joke? (y/n)")
            if hear_joke == "y":
                print_pause("A man goes to the store. His wife says: while you"
                            " are out, get some milk.\n")
                print_pause("He never came home")
                print_pause("")
                print_pause("You laugh")
                print_pause("The machine laughs")
                inventory.append("joke")
                print_pause("The machine thanks you for stopping by and tells"
                            " about some noises by the forest where an "
                            "abandoned machine factory used to operate")
                while True:
                    inv_fact = input("What do you want to do?\n"
                                     "1. Investigate the factory\n"
                                     "2. Go back\n").lower
                    if inv_fact == "1":
                        factory()
                    if inv_fact == "2":
                        game_start()
                    else:
                        print("Please enter a valid option")
            elif hear_joke == "n":
                print_pause("Machine: Sad beeps")
                print_pause("You return to the area you were before")
                game_start()


def factory():
    print_pause("You decided to follow the noise\n"
                "As you approach the forest, you see smoke"
                " coming out of the center of the forest")
    print_pause("You get to the center of the forest and "
                "you find yourself in fornt of a factory")
    print_pause("Inside you find " + boss + " and tries to"
                "attack you")
    while True:
        fact_att_opt = input("What will you do?"
                             "1. Attack back"
                             "2. Run away")

        if fact_att_opt == "1":
            print_pause("You attack the " + factory_boss)
            print_pause(factory_boss + " falls down and you obtain a key code")
            print_pause("Wonder what it would do...")
            inventory.append("key_code")
        if fact_att_opt == "2":
            print_pause("You run back away safely")
            game_start()
        else:
            print("Please enter a valid option")


def ship():
    if "sword" in inventory:
        print_pause("You feel sadness as you see your ship remains")
        print_pause("That was your ship, there were many like"
                    " it but that one was yours")
        print_pause("Theres nothing else to do so you go back")
        game_start()
    else:
        print_pause("You find yourself in front of your ship")
        print_pause("Searching through the remains you find your sword, "
                    + sword)
        inventory.append("sword")
        print_pause("You go back to the area you were before")
        game_start()


def play_again():
    replay = input("Would you like to play again? (y/n)").lower()
    if replay == "y":
        print_pause("Restarting Game")
        inventory.clear()
        play_game()
    elif replay == "n":
        print_pause("Thanks for playing")
    else:
        play_again()


def play_game():
    intro()
    game_start()


play_game()
