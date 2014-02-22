import random
import itertools

Suits = 'cdhs'
Ranks = '23456789TJQKA'

class Deck(object):
	def __init__(self):
		self.CardShoe = tuple(''.join(card) for card in itertools.product(Ranks, Suits))
		self.NumberOfCards = len(self.CardShoe)
		self.Shuffle()
		self.DealOneCard()
#shuffle all 52 cards, return shuffled deck (new CardShoe)
	def Shuffle(self):
		self.ShuffleDeck = random.sample(self.CardShoe, 52)
		
		print "Print shuffleDeck", self.ShuffleDeck


#interaction of the deck class, namely dealing cards to the assigned players
	def DealOneCard(self):
		self.OneCard = (random.sample(self.CardShoe, 1))[0]
		print "Deal card", self.OneCard
		self.ShuffleDeck.remove(self.OneCard)
		print "deck with removed card", self.ShuffleDeck
		return self.ShuffleDeck

		
		
