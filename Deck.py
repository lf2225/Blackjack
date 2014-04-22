import random
import itertools

Suits = 'cdhs'
Ranks = '23456789TJQKA'

class Deck(object):
	def __init__(self):
		print 'I am entering the init routine of Deck'
		self.CardShoe = tuple(''.join(card) for card in itertools.product(Ranks, Suits))
		self.NumberOfCards = len(self.CardShoe)
		self.Shuffle()
		print 'I am exiting the init routine of Deck'


#will be a helper method to be called during gameplay over and over again
#shuffle all 52 cards, return shuffled deck (new CardShoe)
	def Shuffle(self):
		self.ShuffleDeck = random.sample(self.CardShoe, 52)

		print "The shuffled deck is: ", self.ShuffleDeck


#interaction of the deck class, namely dealing cards to the assigned players
	def DealOneCard(self):
		print 'I am at the start of the DealOneCard routine'
		self.OneCard = (random.sample(self.ShuffleDeck, 1))[0]
		print "Deal card", self.OneCard

		self.ShuffleDeck.remove(self.OneCard)

		print "deck with removed card", self.ShuffleDeck
		return self.OneCard
