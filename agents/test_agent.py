class Agent:
    def __init__(self):
        self._remaining_cards = range(1, 13)

    def play_card(self, cardValue):
        return self._remaining_cards.pop()


my_agent = Agent()

print(my_agent._remaining_cards)

