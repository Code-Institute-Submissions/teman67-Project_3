import time
import os

# Define global variables to keep track of items acquired
has_candle = False
has_matches = False
has_knife = False
has_hammer = False
has_rope = False

def welcome_page():
    while True:
        print("\n" + "*" * 80)
        print("""
        __        __   _                            _          _   _          
        \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___ 
         \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \\
          \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/
           \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|
           / \   __| |_   _____ _ __ | |_ _   _ _ __ ___                      
          / _ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \                     
         / ___ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/                     
        /_/   \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|                     
         / ___| __ _ _ __ ___   ___| |                                        
        | |  _ / _` | '_ ` _ \ / _ \ |                                        
        | |_| | (_| | | | | | |  __/_|                                        
         \____|\__,_|_| |_| |_|\___(_)                                        
        """)
        print("*" * 80)
        print("\nPress 'P' to start the game, 'D' for game description, or 'Q' to quit.")

        choice = input().lower()
        if choice == "p":
            main_hall()
        elif choice == "d":
            description_page()
        elif choice == "q":
            exit()
        else:
            print("Invalid choice. Press 'P' to start the game, 'D' for game description, or 'Q' to quit.")

def description_page():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "=" * 50)
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("=" * 50)
    print("\nIn this adventure, you find yourself in a main hall with three doors: left, center, and right.")
    time.sleep(1)
    print("Your goal is to explore the rooms, find a passcode, make right choices, and finally open gold chest to complete the adventure.")
    print("Press 'B' to go back to main page.")
    while True:
        choice = input().lower()
        if choice == 'b':
            welcome_page()
            break  # Exit the loop when returning to the welcome page
        else:
            print("Invalid choice. Press 'B' to go back to the main page.")

def main_hall():
    print("You are in a main hall with three doors: left, center, and right.")
    choice = input("Which door do you choose? (left/center/right): ").lower()

    if choice == "left":
        left_door()
    elif choice == "center":
        center_door()
    elif choice == "right":
        right_door()
    else:
        print("Invalid choice. Try again.")
        main_hall()


def left_door():
    print(
        "You enter a room with a staircase leading down and another door back to the main hall."
    )
    choice = input(
        "Do you want to go down the stairs or back to the main hall? (down/main): "
    ).lower()

    if choice == "down":
        down_stairs()
    elif choice == "main":
        main_hall()
    else:
        print("Invalid choice. Try again.")
        left_door()

def down_stairs():
    if has_candle and has_matches:
        print("You use the candle and matches to light up the room.")
        time.sleep(1)
        print("The room is now illuminated.")
        time.sleep(1)
        print(
            "There is a chest of golds here, but it's locked. You need a passcode to open the chest."
        )
        time.sleep(1)
        password = input("Enter the passcode to open the chest: ")

        if password == "Teman67":
            print("Congratulations! You entered the correct passcode.")
            time.sleep(1)
            print("The chest opens, and you find the golds inside.")
            time.sleep(1)
            display_golden_chest()
            time.sleep(1)
            print("You are now rich! Well done!")
            while True:
                choice = input("Do you want to play again? (y/n): ")
                if choice == "y":
                    main_hall()
                elif choice == "n":
                    print("Thanks for playing!")
                    exit()
                else:
                    print("Invalid choice. Try again!")

        else:
            print("Incorrect password. Try to find the passcode!")
            choice_2 = input(
                "Where do you want to go, upstairs or main hall? (up/main): ").lower(
                )
            if choice_2 == "up":
                left_door()
            elif choice_2 == "main":
                main_hall()
            else:
                print("Invalid choice. Try again!")
                down_stairs()
    else:
        print(
            "It's too dark to see anything. Try to find some items to illuminate the room!"
        )
        time.sleep(1)
        choice_2 = input(
            "Where do you want to go, upstairs or main hall? (up/main): ").lower()
        if choice_2 == "up":
            left_door()
        elif choice_2 == "main":
            main_hall()
        else:
            print("Invalid choice. Try again!")
            down_stairs()


def center_door():
    print(
        "You enter a room with two staircases, one leading up and another door back to the main hall."
    )
    choice = input(
        "Do you want to go up the stairs or back to the main hall? (up/main): "
    ).lower()

    if choice == "up":
        up_stairs()
    elif choice == "main":
        main_hall()
    else:
        print("Invalid choice. Try again.")
        center_door()


def up_stairs():
  print(
      "You climb the stairs and find yourself in a room with a note on the wall. You have 8 seconds to memorize it!"
  )
  time.sleep(1)
  note_message = "The note reads: 'Teman67'"
  print(note_message, end='', flush=True)  # Print without newline and flush the output
  time.sleep(8)
  # Clear the message by printing spaces
  print("\r" + " * " * len(note_message), end='', flush=True)

  print("\nYou memorize the passcode and decide to go back to the main hall.")
  main_hall()


def right_door():
  global has_candle, has_matches, has_knife, has_hammer, has_rope
  items_chosen = 0  # Keep track of the number of items chosen
  print(
      "You enter a big room and see five items: a candle, matches, a knife, a hammer, and a rope."
  )
  time.sleep(1)
  print(
      "Which items do you want to take? You can select three items. Be careful about which items you want to grab!"
  )
  time.sleep(1)
  while items_chosen < 3:
    item_choice = input(
        "Choose an item (candle/matches/knife/hammer/rope): ").lower()
    if item_choice == "candle" and not has_candle:
      has_candle = True
      print("You picked up the candle.")
      items_chosen += 1
    elif item_choice == "matches" and not has_matches:
      has_matches = True
      print("You picked up the matches.")
      items_chosen += 1
    elif item_choice == "knife" and not has_knife:
      has_knife = True
      print("You picked up the knife.")
      items_chosen += 1
    elif item_choice == "hammer" and not has_hammer:
      has_hammer = True
      print("You picked up the hammer.")
      items_chosen += 1
    elif item_choice == "rope" and not has_rope:
      has_rope = True
      print("You picked up the rope.")
      items_chosen += 1
      time.sleep(1)
      display_snake()
      time.sleep(2)
      print("Oh Shit! it is a snake.")
      time.sleep(1)
      print("You try to escape but the snake bites you. Game Over!")
      time.sleep(2)
      print("I told you be careful about which items you want to grab!")
      time.sleep(3)
      while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
          has_candle = False
          has_matches = False
          has_knife = False
          has_hammer = False
          has_rope = False
          main_hall()
          break  # Exit the loop and start a new game
        elif play_again == "n":
          print("Thanks for playing!")
          exit()  # Exit the game completely
        else:
          print("Invalid choice. Choose 'y' or 'n'!")
    else:
      print(
          "Invalid choice. Either you already have this item or it's not one of the available options."
      )

  # After selecting three items, proceed with the encounter with the spider
  print(
      "You have picked up three items and are ready to proceed. Wait! There's a gigantic spider in the room! You have to fight with it!"
  )
  time.sleep(2)
  display_spider()
  # Define the spider's stats
  time.sleep(2)
  if has_knife == True:
    time.sleep(1)
    display_knife()
    time.sleep(2)
    print("You have a knife! You successfully defeat the spider. Good Job!")
    time.sleep(1)
    print(
        "You can now continue to find the gold chest! You go to the main hall")
    main_hall()

  else:
    print("You do not have an item to fight the spider with!")
    time.sleep(1)
    print("You panic and try to escape, but the spiders overwhelm you.")
    time.sleep(1)
    print("Game Over! You have been captured by the spiders.")
    time.sleep(1)
    while True:
      play_again = input("Do you want to play again? (y/n): ").lower()
      if play_again == "y":
        has_candle = False
        has_matches = False
        has_knife = False
        has_hammer = False
        has_rope = False
        main_hall()
        break  # Exit the loop and start a new game
      elif play_again == "n":
        print("Thanks for playing!")
        exit()  # Exit the game completely
      else:
        print("Invalid choice. Choose 'y' or 'n'!")


def display_golden_chest():
    print("""

    █████████           ████      █████             
    ███░░░░░███         ░░███     ░░███              
    ███     ░░░   ██████  ░███   ███████              
    ░███          ███░░███ ░███  ███░░███              
    ░███    █████░███ ░███ ░███ ░███ ░███              
    ░░███  ░░███ ░███ ░███ ░███ ░███ ░███              
    ░░█████████ ░░██████  █████░░████████             
    ░░░░░░░░░   ░░░░░░  ░░░░░  ░░░░░░░░              
                                                    
                                                    
                                                    
    █████████  █████                        █████   
    ███░░░░░███░░███                        ░░███    
    ███     ░░░  ░███████    ██████   █████  ███████  
    ░███          ░███░░███  ███░░███ ███░░  ░░░███░   
    ░███          ░███ ░███ ░███████ ░░█████   ░███    
    ░░███     ███ ░███ ░███ ░███░░░   ░░░░███  ░███ ███
    ░░█████████  ████ █████░░██████  ██████   ░░█████ 
    ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░░     ░░░░░  

    """)
    
def display_spider():
    print("""
     _______  _______ _________ ______   _______  _______ 
    (  ____ \(  ____ )\__   __/(  __  \ (  ____ \(  ____ )
    | (    \/| (    )|   ) (   | (  \  )| (    \/| (    )|
    | (_____ | (____)|   | |   | |   ) || (__    | (____)|
    (_____  )|  _____)   | |   | |   | ||  __)   |     __)
          ) || (         | |   | |   ) || (      | (\ (   
    /\____) || )      ___) (___| (__/  )| (____/\| ) \ \__
    \_______)|/       \_______/(______/ (_______/|/   \__/
                                                          
    """)
  

def display_knife():
  print("""
  
  __,,..,-====>       _,.--''------'' |   _____  ______________`''--._
   \      `\   __..--''                |  /::: / /::::::::::::::\      `\
    \       `''                        | /____/ /___ ____ _____::|    .  \
     \                           ,.... |            `    `     \_|   ( )  |
      `.                       /`     `.\ ,,''`'- ,.----------.._     `   |
        `.                     |        ,'       `               `-.      |
          `-._                 \                                    ``.. /
              `---..............>
  
  """)

def display_snake():
  print("""

             ..=++%%..                
            .:::::-#..                
            **==-=*.                  
            +%==-@#                   
           .+#---%=                   
            =#---+*                   
            .----=.                   
            .+:-+#                    
             +=-=.                    
          ..::--:                     
         ..-:===.                     
    ...#++:-***++*=*++*+*++*+++++-. . 
  ..--:::=*#*##+%%#:=:==:+*%+=%*-%##..
   :.::%%@%%%+++***+*+#+#*#*%**%+*+@*.
    .-=++++*=+*=****#*%##*%%%@##+++=+.
    .::-:++----=-:**+===###++*+*==-:..
       ...:----------=---====-:...    

  """)

# Start the game 
welcome_page()