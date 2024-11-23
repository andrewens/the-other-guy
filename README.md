# the-other-guy
Statistical / game theory analysis on a card game called 'the other guy'

# game rules
1. Three players each have their own suite of cards (hearts, clubs, diamonds) -- i.e. a card for every whole number between 1 and 13.
2. Each turn, a random card from the spades suite is presented for auction. Players must bid for the card:
   1. If two players play the same card, the third player wins the auctioned card
   2. If all players play the same card, no one wins the auctioned card and it's discarded (there are alternatives to this rule, such as adding the auctioned card to the next turn's auction card)
   3. If all players play a different card, the highest card played wins the auctioned card
3. Players with the highest sum of spades cards wins

What is the optimal strategy of play, if any?

# instructions for adding your own agent
1. Have python 3 installed and test that you can run the project by opening a terminal and running `py main.py`
2. To add your own agent:
   1. Create a new file under the `agents` directory. Name it whatever you want
   2. Copy-paste the code from `agents/test_agent.py`. Your agent must match this interface for it to work with the `GameSimulation` object
   3. In `main.py`, line 34 (as of time of writing), a `GameSimulation` object is instantiated with the names of three agent modules to use. You can change any of those to a valid name of any agent module as you like.
   4. Check that `pretty_print_results(...)` (line 37 as of time of writing) is not commented out
   5. Hit run and you should see the results of the simulated game.

If you are curious about how the system as a whole works, try reading the files in the `tests` directory, as they demonstrate how the system works (and is tested).

# TODO
* Support running lots of tests and understanding the distributions of results
* Visualize that data with 3rd party libraries

