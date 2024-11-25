"""
Agent made to thwart the ditto agent by copying the auctioned card and adding one
Will bid 1 on the King(13)
"""

class Agent:
    def __init__(self):
        self._remaining_cards = list(range(1, 14)) # keep track of the cards left in our hand

    def play_card(self, auctioned_card): 
        one_up_index = -1 
    
        one_up = auctioned_card + 1
    
        if one_up in self._remaining_cards:
            one_up_index = self._remaining_cards.index(one_up)
        else:
            # wrap to the remaining number, 1
            # Will always bid one for King a.k.a. 13
            one_up_index = self._remaining_cards.index(1)
        return self._remaining_cards.pop(one_up_index) #Just play whatever the auctioned card is

    
    def round_ended(self, auctioned_card, card_you_played, left_agent_card, right_agent_card, winning_agent):
        # left_agent_card is the card the agent to your left played
        # right_agent_card is the card the agenet to your right played
        # winning_agent is 1 if we won the round, 2 if left_agent won, 3 if right_agent won, or None if no one won

        return

