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
    """Prints the data of the game round"""
    if not last_round:
        print(f"\nYour cards: {player_data['hand']}, current score: {player_data['score']}")
        print(f"Computer's first card: {computer_data['hand'][0]}")
    else:
        print(f"\nYour final hand: {player_data['hand']}, final score: {player_data['score']}")
        print(f"Computer's final hand:  {computer_data['hand']}, final score: {computer_data['score']}\n")

def pick_a_card(data1):
    """Selects a random card form the cards"""
    picked_card =random.choice(cards)

    # Added functionality to update scores to count Ace as 11 or 1
    score=sum(data1['hand']) + picked_card
    if 11 == picked_card and  score> 21:
            picked_card = 1

    elif 11 in data1['hand'] and score > 21:
        for i in range(len(data1['hand'])):
            if data1['hand'][i] == 11 and score > 21:
                data1['hand'][i] = 1
                score-=10
    data1['hand'].append(picked_card)



def initialize_game(data1, data2):
    """Initialzes the game's first round"""
    for i in range(2):
        pick_a_card(data1)
        pick_a_card(data2)
    data1['score'] = sum(data1['hand'])
    data2['score'] = sum(data2['hand'])
    print_round_data(False)

def computer_picks(data):
    """ Checsk if the computer needs more cards and updates the score"""
    while data['score'] <17:
        pick_a_card(data)
        data['score']=sum((data['hand']))


def player_run(p_data,last_round):
    """ Calculate the player score"""
    p_data['score'] = sum(p_data['hand'])
    print_round_data(last_round)
    if p_data['score'] > 21:
        last_round = True
    return last_round


def game_calculation(p_data, c_data, last_round):
        """ Calculates the game round result and prints it"""
        print_round_data(last_round)
        if c_data['score'] == 0:
            print("You Lose! opponent has Blackjack 😱\n")
        elif p_data['score'] == 0:
            print("You Win with a Blackjack 😎\n")
        elif p_data['score'] > 21:
            print("You went over, It's a Bust! You lose. 😭\n")
        elif c_data['score'] > 21:
            print("Opponent went over and got a Bust! You Win. 😁\n")
        elif c_data['score'] > p_data['score']:
            print("You lose 😤\n")
        elif p_data['score'] > c_data['score']:
            print("You win 😃\n")
        else:
            print("It's a Draw 🙃\n")



while game_continue:
    game_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game_input == "n":
        game_continue = False
    else:
        print("\n" * 20)
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

        if computer_data['score'] == 21:
            computer_data['score'] = 0

        if player_data['score'] == 21:
            player_data['score'] = 0

        if computer_data['score'] == 0 or player_data['score'] == 0:
            final_round =True

        while  not final_round:
            round_input = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if round_input == 'y':
                pick_a_card(player_data)
            else:
                final_round = True
            final_round = player_run(player_data, final_round)
            
        if  computer_data['score'] != 0:
            computer_picks(computer_data)
            
        game_calculation(player_data,computer_data,final_round)
