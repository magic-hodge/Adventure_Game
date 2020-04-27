# Imports time for readability.
import time
# Imports random for gambling function.
import random
# Imports math for the money variable.
import math


money = 0
items = []

# Defines the function for printing at a readable speed.


def print_pause(text):
    print(text)
    time.sleep(1)

# Prompts user for reasonable input.


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option == response:
                return response
        print_pause("Please enter a valid response.")
    print_pause(f"You chose {response}.")

# Defines the function to get player's name.


def get_name():
    name = input("Please enter your name.\n")
    print_pause(f"Excellent, {name}. Let's begin.")

# Gets the class user would like to play as, and runs respective class function
# accordingly.
# Wanted to make a second class, so I might in the future.


def get_class():
    response = valid_input("Which class would you like to play as?\n"
                           "1. Gunner\n", ["gunner", "1"])
    if "gunner" in response or "1" in response:
        print_pause("You've chosen the 'gunner' class. Best of luck!")
        # gunner()
    # elif "soldier" in response"
        # print_pause("You've chosen the 'soldier' class. Best of luck!")

# def gunner()

# def soldier()

# Adds money to total.


def money_add(number):
    global money
    money += number
    # return money

# subtracts money from total.


def money_sub(number):
    global money
    money -= number

# adds item to list.


def items_add(item):
    global items
    items.append(item)

# removes item from list.


def items_remove(item):
    global items
    items.remove(item)

# Intorduces Player to game.


def intro():
    print_pause("Welcome to Cool af Game!")
    get_name()
    get_class()
    money_add(100)
    items_add("rifle")
    print_pause("You wake up with a rifle and $100 in your wallet.")

# def money():
    money = 0
    return money

# def items():
    items = []
    return items

# allows Player to choose destination.


def go_somewhere():

    # if Player has map, go_somewhere lists sunken_cave as an option.

    if "map" in items:
        print_pause("Where would you like to go?")
        print_pause("1. Armory.")
        print_pause("2. Town Plaza.")
        print_pause("3. Howling Cave.")
        print_pause("4. Tavern.")
        print_pause("5. Sunken Cave.")

        response = valid_input("Please select a destination.\n",
                               ["armory", "town", "plaza", "howling", "sunken",
                                "tavern", "1", "2", "3", "4", "5"])

        if "armory" in response or "1" in response:
            armory()
        elif "town" in response or "plaza" in response:
            town_plaza()
        elif "2" in response:
            town_plaza()
        elif "howling" in response or "3" in response:
            howling_cave()
        elif "tavern" in response or "4" in response:
            tavern()
        elif "sunken" in response or "5" in response:
            sunken_cave()
# if Player does not have map, the default options are listed in go_somewhere.
    else:
        print_pause("Where would you like to go?")
        print_pause("1. Armory.")
        print_pause("2. Town Plaza.")
        print_pause("3. Howling Cave.")
        print_pause("4. Tavern.")

        response = valid_input("Please select a destination.\n",
                               ["armory", "town", "plaza", "howling", "cave",
                                "tavern", "1", "2", "3", "4"])

        if "armory" in response or "1" in response:
            armory()
        elif "town" in response or "plaza" in response:
            town_plaza()
        elif "2" in response:
            town_plaza()
        elif "howling" in response or "3" in response:
            howling_cave()
        elif "cave" in response:
            howling_cave()
        elif "tavern" in response or "4" in response:
            tavern()

# Player goes to the armory.


def armory():
    print_pause("You step into the armory. "
                "The owner greets you, then questions you in a gruff voice.")

    print_pause("Would you like to buy weapons, sell your rifle, or leave?")
    print_pause("1. Buy Weapons.")
    print_pause("2. Sell Rifle.")
    print_pause("3. Leave.")

    response = valid_input("Please make a selection.\n", ["buy", "sell",
                           "leave", "1", "2", "3"])
    if "buy" in response or "1" in response:
        if "8-Ball" not in items:
            display_money()
            buy_8ball()
        else:
            print_pause("You've already purchased the 8-Ball, so there's "
                        "nothing else to buy.")
    elif "sell" in response or "2" in response:
        display_money()
        sell_rifle()
    elif "leave" in response or "3" in response:
        print_pause("You decide to leave the armory.")
        go_somewhere()
    armory()

# Allows player to sell stock rifle.


def sell_rifle():
    if "rifle" in items:
        response = valid_input("Would you like to sell your rifle for $75?\n"
                               "Please enter 'yes' or 'no'.\n", ["yes", "no"])
        if "yes" in response:
            money_add(75)
            items_remove("rifle")
            print_pause(f"You've sold your rifle and now have ${money}.")
        elif "no" in response:
            print_pause("You've decided not to sell your rifle.")

    else:
        print_pause("You've already sold your rifle.")

# Allows player to buy 8-ball pistol.


def buy_8ball():
    if "8-Ball" not in items:
        response = valid_input("Would you like to purchase the 8-Ball Pistol "
                               "for $100?\n" "Please enter 'yes' or 'no'.\n",
                               ["yes", "no"])
        if "yes" in response:
            if money >= 100:
                money_sub(100)
                items_add("8-Ball")
                print_pause(f"You've purchased the 8-Ball pistol and now have "
                            f"${money}. Lock 'n load!")
            else:
                print_pause("The armory clerk looks at your change and shakes "
                            "his head... " f"You only have ${money}. You "
                            "don't have enough for the 8-Ball.")
        elif "no" in response:
            print_pause("You decide not to buy the 8-Ball.")
    elif "8-Ball" in items:
        print_pause("You've already purchased the 8-Ball, so there's nothing "
                    "else to buy.")

# Player visits town_plaza and has option to buy map.


def town_plaza():
    if "map" not in items:
        print_pause("You wander into the town plaza and see a scruffy "
                    "citizen.")
        response = valid_input("What would you like to do?\n"
                               "1. Speak with the citizen.\n" "2. Leave.\n",
                               ["talk", "speak", "1", "2", "leave"])

        if "talk" in response or "speak" in response:
            print_pause("You strike up a conversation...")
            print_pause("The citizen offers to sell you a treasure map for "
                        "$25.")
            display_money()
            print_pause("Woudl you like to purchase the treasure map?")
            response = valid_input("Please enter yes or no.", ["yes", "no"])
            if 'yes' in response:
                if money >= 25:
                    money_sub(25)
                    items_add("map")
                    print_pause("You've purchased the Map!")
                else:
                    print_pause("The citizen laughs at you and says, "
                                "\'Wow! You're worse off than me, heh. See "
                                "ya, scrub!\'")
            elif 'no' in response:
                print_pause("You've decided not to buy the map. The citizen "
                            "hurries off without even saying goodbye.")
                town_plaza()

        elif "1" in response:
            print_pause("You strike up a conversation...")
            print_pause("The citizen offers to sell you a treasure map for "
                        "$25.")
            response = valid_input("Would you like to purchase the map for "
                                   "$25?\n" "Please enter 'yes' or 'no'.\n",
                                   ["yes", "no"])
            if 'yes' in response:

                if money >= 25:
                    money_sub(25)
                    items_add("map")
                    print_pause("You've purchased the Map!")
                    print_pause(f"You now have ${money}")
                    town_plaza()
                else:
                    print_pause("The citizen laughs at you and says, "
                                "\'Wow! You're worse off than me, heh. "
                                "See ya, scrub!\'")
                    town_plaza()

            elif 'no' in response:
                print_pause("You've decided not to buy the map.\n"
                            "The citizen hurries off without even saying "
                            "goodbye.")
                town_plaza()

        elif "2" in response or "leave" in response:
            print_pause("You leave the plaza.")
            go_somewhere()
    else:
        print_pause("You already have the map, so there's nothing else to do "
                    "in the plaza.")
        go_somewhere()

# Allows player to buy treasure map from citizen.


def buy_map():
    if money >= 25:
        money_sub(25)
        items_add("map")
        print_pause(f"You've purchased the treasure map and now have "
                    f"${money}. Let's get that loot!")
    else:
        print_pause("The townie looks at your change and says... ")
        print_pause(f"You only have ${money}?! Wow. You're worse off than me. "
                    "See ya, scrub!")

# Player explores howling_cave.


def howling_cave():
    print_pause("You find yourself in Howling Cave. An intimidating noise is "
                "coming from within...\n")
    response = valid_input("Would you like to explore further?\n"
                           "1. Explore further.\n" "2. Leave.\n",
                           ["explore", "leave", "1", "2"])
    if "explore" in response or "1" in response:
        fight_werewolf()

    else:
        print_pause("The howling gets louder and closer!!")
        print_pause("Fortunately, you've escaped.")
        go_somewhere()

# Player fights werewolf!


def fight_werewolf():
    print_pause("You journey deeper than you should.")
    print_pause("...")
    print_pause("The werewolf attacks!")
    if "rifle" in items:
        print_pause("The rifle takes too long to load...")
        if "8-Ball" in items:
            print_pause("You take two shots with the 8-Ball pistol, hoping "
                        "they'll do the trick.")
            print_pause("They connect and slow the werewolf down! But the "
                        "werewolf continues its assault.")
            if "9-Breaker" in items:
                print_pause("You prepare the 9-Breaker...")
                if "mercenary" in items:
                    print_pause("Fortunately, the mercenary you hired acts as "
                                "a decoy and tosses you silver bullets.")
                    print_pause("You load the 9-Breaker with the silver "
                                "bullets and shoot to kill.")
                    print_pause("You've slain the werewolf, and the town has "
                                "nothing to fear.\n" "Congratulations, you've "
                                "won!")
                    play_again()
                else:
                    print_pause("But you have no backup and no bullets to "
                                "load it with...")
                    print_pause("You've been slain by the werewolf.")
                    print_pause("Game over.")
                    play_again()
            else:
                print_pause("You have no more weapons...")
                print_pause("You've been slain by the werewolf.")
                print_pause("Game over.")
                play_again()
        elif "9-Breaker" in items:
            if "mercenary" in items:
                print_pause("You try to prepare the 9-Breaker...")
                print_pause("But the werewolf's too quick.")
                print_pause("You and the mercenary have been slain by the "
                            "werewolf.")
                print_pause("If only you had another pistol...")
                print_pause("Game over.")
                play_again()
            else:
                print_pause("You try to prepare the 9-Breaker...")
                print_pause("But you have no bullets and no backup.")
                print_pause("Game over.")
                play_again()
        elif "mercenary" in items:
            if "8-Ball" not in items:
                print_pause("The werewolf's too quick.")
                print_pause("You and the mercenary have been slain by the "
                            "werewolf.")
                print_pause("If only you had more weapons...")
                print_pause("Game over.")
                play_again()
            else:
                print_pause("You have no weapons.")
                print_pause("You and the mercenary have been slain by the "
                            "werewolf.")
                print_pause("Game over.")
                play_again()
        else:
            print_pause("You've been slain by the werewolf.")
            print_pause("Hint: Try exploring or getting more weapons!")
            print_pause("Game over.")
            play_again()
    else:
        if "8-Ball" in items:
            print_pause("You take two shots with the 8-Ball pistol, hoping "
                        "they'll do the trick.")
            print_pause("They connect and slow the werewolf down! But the "
                        "werewolf continues its assault.")
            if "9-Breaker" in items:
                print_pause("You prepare the 9-Breaker...")
                if "mercenary" in items:
                    print_pause("Fortunately, the mercenary you hired acts as "
                                "a decoy and tosses you silver bullets.")
                    print_pause("You load the 9-Breaker with the silver "
                                "bullets and shoot to kill.")
                    print_pause("You've slain the werewolf, and the town has "
                                "nothing to fear.\n" "Congratulations, you've "
                                "won!")
                    play_again()
                else:
                    print_pause("But you have no backup and no bullets to "
                                "load it with...")
                    print_pause("You've been slain by the werewolf.")
                    print_pause("Game over.")
                    play_again()
            else:
                print_pause("You have no more weapons...")
                print_pause("You've been slain by the werewolf.")
                print_pause("Game over.")
                play_again()
        elif "9-Breaker" in items:
            if "mercenary" in items:
                print_pause("You try to prepare the 9-Breaker...")
                print_pause("But the werewolf's too quick.")
                print_pause("You and the mercenary have been slain by the "
                            "werewolf.")
                print_pause("If only you had another pistol...")
                print_pause("Game over.")
                play_again()
            else:
                print_pause("You try to prepare the 9-Breaker...")
                print_pause("But you have no bullets and no backup.")
                print_pause("Game over.")
                play_again()
        elif "mercenary" in items:
            if "8_Ball" not in items:
                print_pause("You have no weapons.")
                print_pause("You and the mercenary have been slain by the "
                            "werewolf.")
                print_pause("If only you had some weapons...")
                print_pause("Game over.")
                play_again()
            else:
                print_pause("You have no weapons.")
                print_pause("You and the mercenary have been slain by the "
                            "werewolf.")
                print_pause("Game over.")
                play_again()
        else:
            print_pause("You've been slain by the werewolf.")
            print_pause("Hint: Try exploring or getting more weapons!")
            print_pause("Game over.")
            play_again()

# Player explores sunken_cave.


def sunken_cave():
    if "9-Breaker" not in items:
        print_pause("You follow the map and come across the location of the "
                    "sunken cave...")
        print_pause("Fortunately, you know exactly where to look and uncover "
                    "the legendary pistol, 9-Breaker.")
        items_add("9-Breaker")
        go_somewhere()
    else:
        print_pause("You've been here before... You already have the "
                    "9-Breaker and there's nothing else in Sunken Cave.")
    go_somewhere()

# clues the player in to the citizen with the map. And Rock, Paper, Scissors.


def gossip():
    print_pause("You sit down at the bar and overhear a conversation...\n")
    print_pause("*Patron 1* Apparently there's a map that reveals the "
                "location of the legendary 9-Breaker pistol. . .\n")
    print_pause("*Patron 2* Oh yeah? Well I hear you have to win $25 at rock, "
                "paper, scissors to beat the game.\n")

# displays Player's current money.


def display_money():

    print_pause(f"You have ${money}.")

# Allows player to order drink.


def order_drink():

    response = valid_input("The bartender asks if you'd like to order a drink "
                           "for $5?\n" "Please say 'yes' or 'no'.\n",
                           ["yes", "no"])
    if "yes" in response:
        if money >= 5:
            money_sub(5)
            print_pause("The bartender takes your order...")
            print_pause(f"You have ${money} left.")
            print_pause("The bartender hands you your favorite drink...")
            print_pause("Ahh - refreshing!")
        else:
            print_pause("I'm sorry. You don't have enough money to order a "
                        "drink.")
    elif 'no' in response:
        print_pause("Alright then. Give me a holler if ya change yer mind!")
    tavern()

# Player enters the tavern, and is able to gamble, hire mercenary, buy a drink,
# gossip, or leave.


def tavern():

    print_pause("You step into the tavern...")
    print_pause("Would you like to order a drink, hire a mecenary, gamble, "
                "gossip, or leave?")
    print_pause("1. Order a drink.")
    print_pause("2. Hire mercenary.")
    print_pause("3. Gamble.")
    print_pause("4. Gossip!")
    print_pause("5. Leave.")

    response = valid_input("Please make a selection.\n",
                           ["drink", "mercenary", "gamble", "gossip", "leave",
                            "1", "2", "3", "4", "5"])

    if "1" in response or "drink" in response:
        display_money()
        order_drink()
    elif "2" in response or "mercenary" in response:
        display_money()
        hire_mercenary()
    elif "3" in response or "gamble" in response:
        rock_paper_scissors()
    elif "4" in response or "gossip" in response:
        gossip()
    elif "5" in response or "leave" in response:
        print_pause("You leave the tavern.")
        go_somewhere()
    tavern()

# Hires mercenary for help.


def hire_mercenary():

    response = valid_input("Would you like to hire a mercenary for $70?\n"
                           "Please enter 'yes' or 'no'.\n", ['yes', 'no'])
    if 'yes' in response:
        if money >= 70:
            money_sub(70)
            print_pause(f"You have ${money} left.")
            items_add("mercenary")
            print_pause("Aight! Now we're talkin'. Where to, Boss?")
        else:
            print_pause("*annoyed gaze*")
            print_pause("You'll need some more coin to chat with me, rookie.")

    elif 'no' in response:
        print_pause("You decide not to hire a mercenary.")
    tavern()

# Lets player gamble at rock, paper, scissors. Sometimes if player loses, it
# doesn't type out full message.


def rock_paper_scissors():
    display_money()
    print_pause("Would you like to play rock, paper, scissors and bet "
                "$25/game?")
    response = valid_input("Please enter 'yes' or 'no'.\n", ["yes", "no"])
    if "yes" in response:
        if money >= 25:
            money_sub(25)
            opponent = ["rock", "paper", "scissors"]
            random.choice(opponent)
            print_pause("Alright!")
            print_pause("What will you choose?")
            print_pause("1. Rock.\n" "2. Paper.\n" "3. Scissors.\n")
            response = valid_input("Please make a selection.\n", ["rock",
                                   "paper", "scissors", "1", "2", "3"])

# response vs. rock.

            if "rock" in response or '1' in response:
                print_pause(f"{response} it is!")
                if random.choice(opponent) == "scissors":
                    print_pause("You chose 'rock'.")
                    print_pause("Your opponent chose 'scissors', so you've "
                                "won!")
                    money_add(50)
                elif random.choice(opponent) == "rock":
                    print_pause("You chose 'rock'.")
                    print_pause("Your opponent also chose 'rock', so it's a "
                                "tie.")
                    money_add(25)
                elif random.choice(opponent) == "paper":
                    print_pause("You chose 'rock'.")
                    print_pause("Your opponent chose 'paper', so you've lost.")

# response vs. paper.

            elif "paper" in response or '2' in response:
                print_pause(f"{response} it is!")

                if random.choice(opponent) == "rock":
                    print_pause("You chose 'paper'.")
                    print_pause("Your opponent chose 'rock', so you've won!")
                    money_add(50)
                elif random.choice(opponent) == "paper":
                    print_pause("You chose 'paper'.")
                    print_pause("Your opponent also chose 'paper', so it's a "
                                "tie.")
                    money_add(25)
                elif random.choice(opponent) == "scissors":
                    print_pause("You chose 'paper'.")
                    print_pause("Your opponent chose 'scissors', so you've "
                                "lost...")

# response vs. scissors.

            elif "scissors" in response or '3' in response:
                print_pause(f"{response} it is!")

                if random.choice(opponent) == "paper":
                    print_pause("You chose 'scissors'.")
                    print_pause("Your opponent chose 'paper', so you've won!")
                    money_add(50)
                elif random.choice(opponent) == "scissors":
                    print_pause("You chose 'scissors'.")
                    print_pause("Your opponent also chose 'scissors', so it's "
                                "a tie.")
                    money_add(25)
                elif random.choice(opponent) == "rock":
                    print_pause("You chose 'scissors'.")
                    print_pause("Your opponent chose 'rock', so you've "
                                "lost...")

            rock_paper_scissors()
        else:
            print_pause("You don't have enough money to play...")
    elif "no" in response:
        print_pause("You decide not to play.")
        tavern()

# Asks to play again. -- Had some weird functionality with the play again
# function if player wins. . .


def play_again():
    print_pause("Would you like to play again?")
    response = valid_input("Please enter 'yes' or 'no'.\n", ["yes", "no"])
    if "yes" in response:
        play_game()
    elif "no" in response:
        print_pause("Okay. Goodbye!")
        exit()

# Plays game.


def play_game():

    global money
    money = 0
    global items
    items = []
    intro()
    go_somewhere()
    play_again()


play_game()
