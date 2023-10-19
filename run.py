import time
import os

# Define global variables to keep track of items acquired
has_candle = False
has_matches = False
has_knife = False
has_hammer = False
has_rope = False

def welcome_page():
    """
    The welcome function is loaded when the user start the game
    """
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
    """
    The description function shows the instruction of the game
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "=" * 80)
    print("Welcome to the Text-Based Adventure Game!")
    print("=" * 80)
    time.sleep(1)
    print("\nIn this adventure, you find yourself in a main hall with three doors: \nleft, center, and right.")
    time.sleep(1)
    print("Your goal is to explore the rooms, find a passcode, make right choices, \nand finally open gold chest to complete the adventure.")
    time.sleep(1)
    print("You can try to enter the correct passcode twice!")
    time.sleep(1)
    print("Press 'B' to go back to main page.")
    while True:
        choice = input().lower()
        if choice == 'b':
            welcome_page()
            break  # Exit the loop when returning to the welcome page
        else:
            print("Invalid choice. Press 'B' to go back to the main page.")

def main_hall():
    """
    The main_hall function is the main entrance to different doors
    """
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
        "You enter a room with a staircase leading down and another \ndoor back to the main hall."
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
    """
    The down_stairs function has the gold chest. User needs a candle and matches to light the room and see the gold chest
    """
    if has_candle and has_matches:
        print("You use the candle and matches to light up the room.")
        time.sleep(1)
        print("The room is now illuminated.")
        time.sleep(1)
        print(
            "There is a chest of golds here, but it's locked. \nYou need a passcode to open the chest."
        )
        time.sleep(1)
        while True:
            ask_password=input("Do you want to enter the passcode? (y/n): ").lower()
            time.sleep(1)
            if ask_password == "y":
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
                    time.sleep(1)
                    print("Incorrect password. Try to find the passcode!")
                    time.sleep(1)
                    while True:
                        choice_1 = input("do you want to enter the passcode again? (y/n): ").lower()
                        if choice_1 == 'n':
                            choice_2 = input(
                                "Where do you want to go, upstairs or main hall? (up/main): ").lower(
                                )
                            if choice_2 == "up":
                                time.sleep(1)
                                left_door()
                            elif choice_2 == "main":
                                time.sleep(1)
                                main_hall()
                            else:
                                print("Invalid choice. Try again!")
                                time.sleep(1)
                                down_stairs()
                        elif choice_1 == 'y':
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
                                    time.sleep(1)
                                    choice = input("Do you want to play again? (y/n): ")
                                    if choice == "y":
                                        main_hall()
                                    elif choice == "n":
                                        time.sleep(1)
                                        print("Thanks for playing!")
                                        exit()
                                    else:
                                        time.sleep(1)
                                        print("Invalid choice. Try again!")
                            else:
                                time.sleep(1)
                                print("You enter the incorrect passcode twice. No more chance to enter the passcode. Game Over!")
                                while True:
                                    time.sleep(1)
                                    choice = input("Do you want to play again? (y/n): ")
                                    if choice == "y":
                                        main_hall()
                                    elif choice == "n":
                                        time.sleep(1)
                                        print("Thanks for playing!")
                                        exit()
                                    else:
                                        print("Invalid choice. Try again!")
                        else:
                            time.sleep(1)
                            print("Invalid choice. Try again!")
            elif ask_password == 'n':
                time.sleep(1)
                while True:
                    ask_go = input('Where do you want to go? (up/main): ').lower()
                    time.sleep(1)
                    if ask_go == "up":
                        left_door()
                    elif ask_go == "main":
                        main_hall()
                    else:
                        print("Invalid choice. Try again!")
            else:
                print("Invalid choice. Try again!")
            
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
    """
    The center function has the passcode of the gold chest. User has to memorize the code in 8 sec
    """
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
      "You climb the stairs and find yourself in a room with a note on the wall. \nYou have 10 seconds to memorize it!"
  )
  time.sleep(1)
  note_message = "The note reads: 'Teman67'"
  print(note_message, end='', flush=True)  # Print without newline and flush the output
  time.sleep(10)
  # Clear the message by printing spaces
  print("\r" + " * " * len(note_message), end='', flush=True)

  print("\nYou memorize the passcode and decide to go back to the main hall.")
  main_hall()


def right_door():
  """
  The right_door function is a place where user can grab items. The user should be grab correct items to fight with spider and light the room
  """
  global has_candle, has_matches, has_knife, has_hammer, has_rope
  has_candle = False
  has_matches = False
  has_knife = False
  has_hammer = False
  has_rope = False
  items_chosen = 0  # Keep track of the number of items chosen
  time.sleep(1)
  print(
      "You enter a big room and see five items: \na candle, matches, a knife, a hammer, and a rope."
  )
  time.sleep(3)
  print(
      "Which items do you want to take? You can select three items. \nBe careful about which items you want to grab!"
  )
  time.sleep(2)
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
  time.sleep(1)
  print(
      "You have picked up three items and are ready to proceed. \nWait! There's a gigantic spider in the room! You have to fight with it!"
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
    time.sleep(1)
    main_hall()

  else:
    print("Your hammer isn't of much use in a battle against the spider!")
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