logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bidding_data ={}
bid_continue="yes"
max_bid=0
max_bidder=""
no_winner=False

while bid_continue =="yes":
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    bidding_data[name]=int(bid)
    bid_continue = input("Are there any other bidders? Type 'yes' to continue with other bidders.\n").lower()
    print("\n" * 100)

for key in bidding_data:
    if bidding_data[key] == max_bid and max_bid > 0:
        no_winner=True
    elif bidding_data[key] > max_bid:
        max_bid=bidding_data[key]
        max_bidder=key

if not no_winner:
    print(f"The winner is {max_bidder} with a bid of ${max_bid}")
else:
    print(f"The winner could not be decided as there were multiple candidates with same bids")