"""
Agent That copies the auctioned card
"""

class Agent:
    def __init__(self, num_cards_per_suite):
        self._remaining_cards = list(range(1, num_cards_per_suite + 1)) # keep track of the cards left in our hand

    def play_card(self, auctioned_card):
        
        if auctioned_card in self._remaining_cards:
            ditto_index = self._remaining_cards.index(auctioned_card)
        else:
            print("I'm not playing with a full deck.")

        return self._remaining_cards.pop(ditto_index) #Just play whatever the auctioned card is
        
    
    def round_ended(self, auctioned_card, card_you_played, left_agent_card, right_agent_card, winning_agent):
        # left_agent_card is the card the agent to your left played
        # right_agent_card is the card the agent to your right played
        # winning_agent is 1 if we won the round, 2 if left_agent won, 3 if right_agent won, or None if no one won

        return

