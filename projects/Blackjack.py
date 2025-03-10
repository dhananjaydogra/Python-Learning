import random

logo='''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |                
      `------'                           |__/           
      
'''
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_continue = True
user_input=''

while game_continue:
    print(logo)
    
    player_hand =[]
    computer_hand = []
    player_score=0
    computer_score=0

    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    player_score=sum(player_hand)

    computer_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
    computer_score=sum(computer_hand)

    print(f"Your cards: {player_hand}, current score: {player_score}")

    print(f"Computer's first card: {computer_hand[0]}")
    next_card= True
    while next_card:
        round_input=input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if round_input == 'y':
            player_hand.append(random.choice(cards))
            player_score=sum(player_hand)
        else:
            next_card= False

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    if computer_score > player_score or player_score > 21:
        print("You lose 😤")
    elif player_score > computer_score or computer_score > 21:
        print("You win 😁")
    else:
        print("It's a draw")

    game_input=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game_input == "n":
        game_continue=False

