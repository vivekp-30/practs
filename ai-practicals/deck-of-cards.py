import itertools
import random

#Create a deck of cards
suits = ['Spade', 'Heart', 'Diamond', 'Club']
ranks = range(1, 14)
deck = list(itertools.product(ranks, suits))

#Shuffle the deck
random.shuffle(deck)

#Draw five cards
print("You got:")
for i in range(5):
    rank, suit = deck[i]
    print(f"{rank} of {suit}")
