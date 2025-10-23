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
    index = index // 5
    match (index):
        case 1 :
            print("Its An American Brand")
        case 2 :
            print("Its A German Brand") 
        case 3:
            print("Its A Frensh Brand")
        case 4:
            print("Its An English Brand")
        case 5:
            print("Its An Italian Brand")
        case 6:
            print("Its A Japanese Brand")                   

def display_anwser (anwser):
    print(" ".join(anwser))

def start_new_game():
    new_game = True
    while new_game:
        print ("\nDo you want to start new game")
        print ("\n[1] new game")
        print ("\n[2] exit ...")
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
        display_man (wrong_guess)
        display_hint (hint)

        guess = input("\nEnter your letter : ").lower()

        if not len(guess)==1 :
            print(" \nPut one letter ")
            continue

        elif guess == "*":
            display_ultra_hint(anwser)
            use_ultra_hint = True
            continue

        elif not guess.isalpha():
            print (" \nEnter a letter")
            continue

        elif guess in guessed_letter:
            print ("\nIts already guessed")
            continue

        guessed_letter.add(guess)


        if guess in anwser :
            for i in range(len(anwser)):
                if anwser[i] == guess : 
                    hint[i] = guess

        else :
            wrong_guess += 1

        if "_" not in hint:
            print("\nYOU WIN BRO...")
            time.sleep(1)
            print("\nMission complete")
            time.sleep(1)
            print("\nRespect + ")
            time.sleep(1)
            break

        elif wrong_guess >= len(hangman_art)-1 :
            print("\nYOU LOSE BRO...")
            time.sleep(1)
            print("\nMission failue")
            time.sleep(1)
            break

        time_end = time.time()
        time_playing = time_end - time_start

        print("============================================")
        print("\nStatistics :")
        print(f"\n[+] Time playing : {time_playing}")
        time.sleep(1)
        print(f"\nThe correct anwser is :{anwser}")
        time.sleep(1)
        print(f"\nNumber of wrong guesses : {wrong_guess}")
        time.sleep(1)
        print(f"\nAttempts left: {len(hangman_art)-1-wrong_guess}")
        time.sleep(1)
        print(f"\nDid you use the ultra hint : {use_ultra_hint }")
        time.sleep(1)
        print("============================================")
        


if __name__ == "__main__":
    game()
    start_new_game()
    print("Thanks for playing :) ")