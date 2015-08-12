from Deck import Deck
from Hand import Hand


Deck_one = Deck()
try:
    number_of_hands = int(raw_input("How many hands would you like dealt (max 10 per deck)?  "))
except (ValueError, TypeError):
    print "Enter a valid number less or equal to 10"
else:
    hand_obj_list = [Hand() for x in range(number_of_hands)]

    for hand in hand_obj_list:

        #Player1
        hand.deal_hand(Deck_one)

        #print 'a sample player (1) hand', obj.PlayerHand
        hand.display_hand_value()

        #print 'the value of (1) hand is', obj.TotalHandValue
        #prints total hand value of two dealt cards
        hand.add_card(Deck_one)
        print 'the End hand value is', hand.TotalHandValue, "\n\n"

    print 'The rest of the deck is', Deck_one.ShuffledDeck
