import time
import os

def welcome_page():
    while True:
        print("\n" + "*" * 50)
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
        print("*" * 50)
        print("\nPress 'P' to start the game, 'D' for game description, or 'Q' to quit.")

        choice = input().lower()
        if choice == "p":
            break
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
    print("Your goal is to explore the rooms, find a passcode, and make choices to complete the adventure.")
    print("Press 'B' to go back to main page.")
    while True:
        choice = input().lower()
        if choice == 'b':
            welcome_page()
            break  # Exit the loop when returning to the welcome page
        else:
            print("Invalid choice. Press 'B' to go back to the main page.")

welcome_page()