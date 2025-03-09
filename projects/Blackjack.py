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
    
    player_hand = []
    computer_hand = []
    player_score=0
    computer_score=0

    print(f"Your cards: {player_hand}, current score: {player_score}")

    print(f"Computer's first card: {computer_hand[0]}")

    round_input=input("Type 'y' to get another card, type 'n' to pass: ").lower


    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")


    game_input=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if game_input == "n":
        game_continue=False

