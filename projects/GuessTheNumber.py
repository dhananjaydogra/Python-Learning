import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
def guess_the_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1,100)
    lives=10
    #print (f"Hint: {number_to_guess}")
    mode= input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if mode=='hard':
        lives=5

    while lives >0:

        print(f"You have {lives} attempts remaining to guess the number.")
        guessed_number=0
        guess= input("Make a guess: ")
        if guess.isnumeric():
            guessed_number=int(guess)
        if guessed_number == 0:
            lives -= 1
        elif guessed_number < number_to_guess:
            lives -= 1
            print("Too Low.")
        elif guessed_number > number_to_guess:
            lives -= 1
            print("Too High.")
        else:
            lives=-2
            print(f"You got it! The answer was {number_to_guess}.")
        if lives > 0:
            print("Guess again.")
    if lives==0:
        print("You've run out of guesses.")

game_round = True

while game_round:
    guess_the_number()
    check=input("Do you want to start the game again? Type 'yes' to restart : ").lower()
    if check == "yes":
        game_round = True
        print("\n" * 20)
    else:
        game_round = False
