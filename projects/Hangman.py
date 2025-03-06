import random
import Hangman_art
import Hangman_words

lives = 6

print(Hangman_art.logo)
chosen_word = random.choice(Hangman_words.word_list)
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
display = ""
while not game_over:


    print(f"****************************<{lives}>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"\n\nThe word was: {chosen_word}.\n*********************** You Lose. **********************")

    if "_" not in display:
        game_over = True
        print("\n**************************** You Win! ****************************")

    print(Hangman_art.stages[lives])



#Other logic to complete it
# words_guessed = 0
# lives = 6
# print("Word to guess: " + placeholder)
# while words_guessed != word_length:
#     print(f"****************************<{lives}>/6 LIVES LEFT****************************")
#     guess = input("Guess a letter: ").lower()
#     if guess in display:
#         print(f"You have already guessed {guess}")
#     display = ""

#     for letter in range(word_length):
#         if chosen_word[letter] == guess:
#             display += chosen_word[letter]
#             words_guessed += 1
#         elif placeholder[letter] != "_" :
#              display += placeholder[letter]
#         else:
#             display += "_"

#     placeholder=display
#     print(display)

#     if guess not in chosen_word:
#         lives -= 1
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#     if lives == 0:
#         words_guessed=word_length
#         print(f"The word was: {chosen_word}.\n*********************** You Lose. **********************")

#     if display==chosen_word:
#         print("**************************** You Win! ****************************")

#     print(Hangman_art.stages[lives])