import random


cards=['s','e','r','y']
ranks=range(1,14)
decks=[(rank,card) for rank in ranks for card in cards]


print("You Got")
for rank,deck in decks[:5]:
    print(f"{rank} of {deck}")
