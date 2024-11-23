import random

class Agent:
    def __init__(self):
        self._remaining_cards = list(range(1, 14)) # keep track of the cards left in our hand

    def play_card(self, auctioned_card):
        random_index = random.randint(0, len(self._remaining_cards) - 1)
        return self._remaining_cards.pop(random_index) # pick a random card in our hand

