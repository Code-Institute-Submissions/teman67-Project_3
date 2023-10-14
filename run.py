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
    print("You enter a room filled with giant spiders!")
    display_spider()
    time.sleep(1)
    print("You panic and try to escape, but the spiders overwhelm you.")
    time.sleep(1)
    print("Game Over! You have been captured by the spiders.")

    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again == "y":
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
  

# Start the game 
welcome_page()