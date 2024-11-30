# the-other-guy
Statistical / game theory analysis on a card game called 'the other guy'

# game rules
1. Three players each have their own suite of cards (hearts, clubs, diamonds) -- i.e. a card for every whole number between 1 and 13. ([Hyp] Ace is 1, Jack is 11, Queen is 12, and King is 13)
2. Each turn, a random card from the spades suite is presented for auction. Players must bid for the card:
   1. If two players play the same card, the third player ("the-other-guy" [Hyp]) wins the auctioned card
   2. If all players play the same card, no one wins the auctioned card and it's discarded (there are alternatives to this rule, such as adding the auctioned card to the next turn's auction card)
   3. If all players play a different card, the highest card played wins the auctioned card ([Hyp] Suggestion from Burt, put this rule first as it's most common)
3. Players with the highest sum of spades cards wins
4. [Hyp] Alternative to cards, this game can be played online.  Where the "cards" are 1 to n where n does not have to be 13.

What is the optimal strategy of play, if any? [Hyp -- Burt adds, there is a Nash equilibrium, which will be a mixed strategy.  I.e. not deterministic.  We're looking for an ESS {Evolutionary Stable Strategy).  Every ESS is a Nash equilibrium but not every Nash is ESS. 

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
* (1) Support running lots of tests and understanding the distributions of results
* Visualize that data with 3rd party libraries
* [Hyp] Add agent names to printout, double check current agents
* [Hyp] Brainstorm other simple strategy agents, add
* [Hyp] Other than win/loss and scores, figure out if these are the only stats we care about  (other possibilities include bid differentials for each player for each round)
* [Hyp] Extension of (1) After brainstorms, wrapper to run main.py many times with each combination of players and collect stats in csv for records -> then averaging, t-tests to test for differences, stddev and matplotlib for beauty
* [Hyp] Discuss theme music

# Interesting questions / observations
* The possible number of unique games is `13^4 x 12^4 x 11^4 x ... x 2^4 x 1^4 = 1.5035617E39`. Do you think if we reduced the number of possible cards in play, and mapped the decision tree for that, the patterns would be the same as they are for 13 card suites?
* The sum of all the cards in a suite is 91. So to guarantee that you win, you have to get a sum of 46 cards. So it might make sense to have some sort of strategy where you throw on some turns in order to conserve purchasing power, and also it's possible for the game to be decided before it's over. Also if you keep track of your opponents' cards you could use that information to guarantee a win (i.e. if you know that they don't have a certain card, you can play that card, and in some cases you might be able to guarantee that you have the highest card). Do you think we could still map the tree of all outcomes but just thinking in higher order rules instead of every explicit outcome?
* But, I think the complexity space is reduced by psychology.  If we were looking at a ton of random agents, then yeah, overwhelming and maybe boring.  But the strategy will reduce that space, maybe to significantly smaller.  If you are playing the auctioned card for instance, your complexity contribution is 1x1x1x...x1.
* When is it optimal to bet that you will win this game? Is it at 31?
* Let's say that you have the entire space of all possible games, but you exclude all of the turns after a player gets 46 points. What % of the turns do you think that would exclude in the space
