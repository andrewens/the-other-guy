import random

class Agent:
    def __init__(self, num_cards_per_suite):
        self._remaining_cards = list(range(1, num_cards_per_suite + 1)) # keep track of the cards left in our hand

    def play_card(self, auctioned_card):
        random_index = random.randint(0, len(self._remaining_cards) - 1)
        return self._remaining_cards.pop(random_index) # pick a random card in our hand
    
    def round_ended(self, auctioned_card, card_you_played, left_agent_card, right_agent_card, winning_agent):
        # left_agent_card is the card the agent to your left played
        # right_agent_card is the card the agent to your right played
        # winning_agent is 1 if we won the round, 2 if left_agent won, 3 if right_agent won, or None if no one won

        return


