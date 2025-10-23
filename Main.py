import random
import time
import subprocess
import os


words = (
    # USA
    "Ford", "Chevrolet", "Tesla", "Dodge", "Jeep",
    
    # Germany
    "BMW", "Mercedes-Benz", "Audi", "Porsche", "Volkswagen",
    
    # France
    "Peugeot", "Renault", "Citroën", "Bugatti", "DS",
    
    # UK
    "Aston Martin", "Rolls Royce", "Bentley", "Jaguar", "Land Rover",
    
    # Italy
    "Ferrari", "Lamborghini", "Maserati", "Alfa Romeo", "Fiat",
    
    # Japan
    "Toyota", "Honda", "Nissan", "Mazda", "Subaru"
)

#print(words)

colors = [
    "\033[30m",  # Black                0
    "\033[31m",  # Red                  1
    "\033[32m",  # Green                2
    "\033[33m",  # Yellow               3
    "\033[34m",  # Blue                 4
    "\033[35m",  # Magenta              5
    "\033[36m",  # Cyan                 6
    "\033[37m",  # White                7
    "\033[90m",  # Bright Black (Gray)  8
    "\033[91m",  # Bright Red           9
    "\033[92m",  # Bright Green         10
    "\033[93m",  # Bright Yellow        11
    "\033[94m",  # Bright Blue          12
    "\033[95m",  # Bright Magenta       13
    "\033[96m",  # Bright Cyan          14
    "\033[97m",  # Bright White         15
    "\033[0m"    # Reset (Default color)16
]


hangman_art =           {0: (      "   ",
                                   "   ",
                                   "   "),
                             1: (" o ",
                                   "   ",
                                   "   "),
                             2: (" o ",
                                   " | ",
                                   "   "),
                             3: (" o ",
                                   "/| ",
                                   "   "),
                             4: (" o ",
                                  "/|\\",
                                   "   "),
                              5: (" o ",
                                   "/|\\",
                                   "/  "),
                              6: (" o ",
                                   "/|\\",
                                   "/ \\")}



def display_man (wrong_guess):

    print("=================")
    for l in hangman_art[wrong_guess]:
        print (l)

    print("=================")    

def display_hint (hint):
    print(" ".join(hint))


def display_ultra_hint (anwser):
    index = 0
    for i in words:
        index += 1
        if i == anwser:
            break
    index = (index - 1) // 5

    match (index):
        case 1 :
            print(f"{colors[2]}Its An {colors[4]}American Brand{colors[7]}{colors[16]}")
        case 2 :
            print(f"{colors[0]}Its A {colors[3]}German Brand{colors[1]}{colors[16]}") 
        case 3:
            print(f"{colors[4]}Its A {colors[7]}Frensh Brand{colors[1]}{colors[16]}")
        case 4:
            print(f"{colors[4]}Its An {colors[7]}English Brand{colors[1]}{colors[16]}")
        case 5:
            print(f"{colors[2]}Its An {colors[7]}Italian Brand{colors[1]}{colors[16]}")
        case 6:
            print(f"Its A {colors[7]}Japanese Brand{colors[1]}{colors[16]}")                   

def display_anwser (anwser):
    print(" ".join(anwser))

def start_new_game():
    new_game = True
    while new_game:
        print ("\nDo you want to start new game")
        print (f"\n{colors[2]}[1] new game{colors[16]}")
        print (f"\n{colors[1]}[2] exit ...{colors[16]}")
        choice = input("> ")
        match (choice):
            case "1":
                game()
            case "2":
                new_game = False
            case _ :
                print("Invalid choice!")    
        
    

def game ():
    anwser = random.choice(words).lower()
    print(anwser)

    hint = ["_" if c.isalpha() else c for c in anwser]
    wrong_guess = 0
    guessed_letter = set()
    use_ultra_hint = False


    print("Welcome to Hangman Game")
    time.sleep(1)
    print("The game is gonna start after :")
    print("3...",end="\r")
    time.sleep(1)
    print("2...",end="\r")
    time.sleep(1)
    print("1...",end="\r")
    time.sleep(1)
    print("Goooooo ...")
    subprocess.run('cls' if os.name =='nt' else 'clear' , shell=True)
    time_start = time.time()
    

    while True:
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        display_man (wrong_guess)
        display_hint (hint)

        guess = input("\nEnter your letter : ").lower()
        print("\nTo use ultra Hint put * ")

        if not len(guess)==1 :
            print(f" \n{colors[16]}Put one letter {colors[16]}")
            print("\nTo use ultra Hint put * ")
            continue

        elif guess == "*":
            display_ultra_hint(anwser)
            use_ultra_hint = True
            continue

        elif not guess.isalpha():
            print (f" \n{colors[1]}Enter a letter{colors[16]}")
            print("\nTo use ultra Hint put * ")
            continue

        elif guess in guessed_letter:
            print (f"\n{colors[1]}Its already guessed{colors[16]}")
            print("\nTo use ultra Hint put * ")
            continue

        guessed_letter.add(guess)


        if guess in anwser :
            for i in range(len(anwser)):
                if anwser[i] == guess : 
                    hint[i] = guess

        else :
            wrong_guess += 1

        if "_" not in hint:
            print(f"\n{colors[2]}YOU WIN BRO...{colors[16]}")
            time.sleep(1)
            print(f"\n{colors[2]}Mission complete{colors[16]}")
            time.sleep(1)
            print("\nRespect + ")
            time.sleep(1)
            break

        elif wrong_guess >= len(hangman_art)-1 :
            print(f"\n{colors[16]}YOU LOSE BRO...{colors[16]}")
            time.sleep(1)
            print(f"\n{colors[16]}Mission failue{colors[16]}")
            time.sleep(1)
            break

    time_end = time.time()
    time_playing = round(time_end - time_start, 2)

    print("============================================")
    print("\nStatistics :")
    print(f"[+] Time playing : {time_playing} seconds")
    time.sleep(1)
    print(f"[+] The correct anwser is :{anwser}")
    time.sleep(1)
    print(f"[+] Number of wrong guesses : {wrong_guess}")
    time.sleep(1)
    print(f"[+] Attempts left: {len(hangman_art)-1-wrong_guess}")
    time.sleep(1)
    print(f"[+] Did you use the ultra hint : {use_ultra_hint }")
    time.sleep(1)
    print("============================================")
        


if __name__ == "__main__":
    game()
    start_new_game()
    print("Thanks for playing :) ")