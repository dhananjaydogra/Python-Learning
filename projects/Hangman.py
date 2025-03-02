import random

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')
wordlist=["aardvark", "baboon", "camel","test","help","mark"]
word=random.choice(wordlist)
guessed_word=[]
for i in word:
    guessed_word+='_'

lives=6
word_found=len(word)
while lives>0:
    printguess="".join(guessed_word)
    print(f"Word to guess: {printguess}")
    guess_letter=input("Guess a letter :   ")
    letter_found=False
    for i in range(len(word)):
        if str.lower(guess_letter)==str.lower(word[i]):
            guessed_word[i]=word[i]
            letter_found=True
            word_found-=1
    if not letter_found:
        lives-=1
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
    if word_found==0:
        print(f"You Win!! \nThe word is {word}")    
        lives=0
    elif lives>0:
        print(f"****************************{lives}/6 LIVES LEFT****************************")        
    else:
        print(f"***********************The word was {word}! YOU LOSE**********************")