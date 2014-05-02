from Deck import *
from Hand import *

Deck_one = Deck()
obj_list = [Hand() for x in range(6)]

for obj in obj_list:

    #Player1

    obj.deal_hand(Deck_one)

    #print 'a sample player (1) hand', obj.PlayerHand

    obj.display_hand_value()

    #print 'the value of (1) hand is', obj.TotalHandValue

    #prints total hand value of two dealt cards
    obj.add_card(Deck_one)



    print 'the new hand value is', obj.TotalHandValue, "\n"



    #for i in range(1,53):
    #	Deck1.DealOneCard()

print 'print the rest of the deck', Deck_one.ShuffledDeck
