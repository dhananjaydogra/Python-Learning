import random

from HigherLowerGameData import data

logo ="""
    __  ___       __                     
   / / / (_)___ _/ /_  ___  _____     
  / /_/ / / __ '/ __ \/ _ \/ ___/	 
 / __  / / /_/ / / / /  __/ / 	 __
/_/ ///_/\__, /_/ /_/\___/_/    / /   ____ _      __ __  _____
        /____/                 / /   / __ \ | /| / / _ \/ ___/
							  / /___/ /_/ / |/ |/ /  __/ /  
							 /_____/\____/|__/|__/\___/_/   """

vs= """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

score=0
game_continue=True

def fetch_game_detail (item):
    """Pick a random item from the data set excluding the previous selection"""
    item2 = random.choice(data)
    while item == item2:
        item2 = random.choice(data)
    return item2

def check_comparison(item,item2,picked_item):
    """it used to check the users choice with the data """
    print (picked_item)
    if picked_item == 'a' and item['follower_count'] > item2['follower_count']:
        return True
    elif picked_item == 'b' and item['follower_count'] < item2['follower_count']:
        return True
    else:
        return False

def print_score(flag):
    """Used to print the score of the game based on correct and incorrect scenario"""
    if flag:
        print("\n" * 100)
        print(logo)
        print(f"You are right! Current Score: {score}.")
    else:
        print("\n" * 100)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    return False

print(logo)
data1=fetch_game_detail("")
data2=fetch_game_detail(data1)

while game_continue:

    print(f"\nCompare A: {data1['name']}, a {data1['description']}, from {data1['country']} {vs} \nCompare B: {data2['name']}, a {data2['description']}, from {data2['country']}")
    selected_value = input("Who has more followers? Type 'A' or 'B' : ").lower()
    if check_comparison(data1,data2,selected_value):
        score += 1
        data1 = data2
        data2 = fetch_game_detail(data1)
        print_score(True)
    else:
        game_continue=print_score(False)