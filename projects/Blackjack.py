import random

logo = '''
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
user_input = ''

def print_round_data(last_round):
    if not last_round:
        print(f"Your cards: {player_data['hand']}, current score: {player_data['score']}")
        print(f"Computer's first card: {computer_data['hand'][0]}")
    else:
        print(f"Your final hand: {player_data['hand']}, final score: {player_data['score']}")
        print(f"Computer's final hand:  {computer_data['hand']}, final score: {computer_data['score']}")

def pick_a_card(data1):
    data1['hand'].append(random.choice(cards))


def initialize_game(data1, data2):
    for i in range(2):
        pick_a_card(data1)
        pick_a_card(data2)
    data1['score'] = sum(data1['hand'])
    data2['score'] = sum(data2['hand'])
    print_round_data(False)

def computer_picks(data):
    while data['score'] <=17:
        pick_a_card(data)
        data['score']=sum((data['hand']))

#Create a Function to update scores to count Ace as 11 or 1

def game_calculation(p_data, c_data, last_round):

    #Calculate the player score
    p_data['score'] = sum(p_data['hand'])

    if not last_round:
        print_round_data(last_round)
    else:
        print_round_data(last_round)
        if (c_data['score'] > p_data['score'] and c_data['score'] <=21) or p_data['score'] > 21 or c_data['score'] == 21:
            print("You lose 😤")
        elif p_data['score'] > c_data['score'] or c_data['score'] > 21 or p_data['score'] == 21:
            print("You win 😃")
        else:
            print("It's a Draw 🙃")



while game_continue:
    print(logo)
    player_data= {
        "hand" : [],
        "score" : 0,
    }
    computer_data= {
        "hand" : [],
        "score" : 0,
    }
    final_round = False

    initialize_game(player_data, computer_data)
    computer_picks(computer_data)
    while  not final_round:
        round_input = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if round_input == 'y':
            pick_a_card(player_data)
        else:
            final_round = True
        game_calculation(player_data, computer_data, final_round)


    game_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game_input == "n":
        game_continue = False

