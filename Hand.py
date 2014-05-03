from Deck import *

UserDecision = ""

#move this to the main program later
def user_input():
		global UserDecision = str(raw_input("H or S? "))
		print 'You said you want to ', UserDecision


ValueDict = {'2':2,
			 '3':3,
			 '4':4,
			 '5':5,
			 '6':6,
			 '7':7,
			 '8':8,
			 '9':9,
			 'T':10,
			 'J':10,
			 'Q':10,
			 'K':10,
			 'A':11}

class Hand(object):
	def __init__(self):
		#print 'I am entering the init routine of Hand'
		self.TotalHandValue = 0
		self.PlayerHand = []
		#print 'I am exiting the init routine of Hand'


#initial dealing of the hand, calls the AddCard method twice
	def deal_hand(self, Deck1):
		global InitialHandDecision
		Card1 = Deck1.deal_one_card()
		Card2 = Deck1.deal_one_card()
		print Card1, Card2
		self.PlayerHand = [Card1, Card2]
		InitialHandDecision = user_input()




#helper method to figure out the value of aces in hand
	def ace_count(self):
		HighAce = False
		if len(self.PlayerHand) <= 2:
			if UserDecision = print 'I have two cards'
			for card in self.PlayerHand:
				#one ace in the initial hand, always ace high
				if ValueDict[self.PlayerHand[0][0]] == 11 or ValueDict[self.PlayerHand[1][0]] == 11:
					HighAce = True
					if ValueDict[self.PlayerHand[0][0]] == 11 and ValueDict[self.PlayerHand[1][0]] == 11:
						#set one to 11, set the other to 1, no order required
						HighAce = True
						ValueDict[self.PlayerHand[1][0]] == 1
		else:
			#if total is more than 21, reduce all aces to 1
			print "I have more than two cards"
			for card in self.PlayerHand:
				if self.TotalHandValue > 21:
					for card in self.PlayerHand:
						number_of_aces = 0
						if ValueDict[card[0]] == 11:
							number_of_aces += 1
							print "I have", number_of_aces, "aces"
							HighAce = False
							self.TotalHandValue = self.TotalHandValue - 10
							print 'Aces have been reduced from 11 to 1'

							if ((self.TotalHandValue - 10) < 10):
								HighAce = True
								self.TotalhandValue = self.TotalHandValue + 10
								print 'It made sense to up one ace to 11'



	def five_card_charlie(self):
		#tests if self.PlayerHand reached 5 cards.  helper method to be called from add_card routine
		if len(self.PlayerHand) == 5:
			return True
		else:
			return False


#conveniently display the status of a hand
#initialize the dictionary  (J, Spades...) = (11,1...)
	def display_hand_value(self):
		self.ace_count()
		TotalHandValue = 0
		for card in self.PlayerHand:
			# ValueCard1 = ValueDict[self.PlayerHand[0][0]]
			# ValueCard2 = ValueDict[self.PlayerHand[1][0]]
			TotalHandValue += ValueDict[card[0][0]]


		'''if self.TotalHandValue <= 16 and Card1[0] == 'A':
			ValueCard1 = ValueDict[Card1[0]][1]
		elif self.TotalHandValue <= 16 and Card2[0] == 'A':
			ValueCard2 = ValueDict[Card2[0]][1]
		elif self.TotalHandValue > 16 and Card1[0] == 'A':
			ValueCard1 = ValueDict[Card1[0]][0]
		elif self.TotalHandValue > 16 and Card2[0] == 'A':
			ValueCard2 = ValueDict[Card2[0]][0]'''
		# self.ace_count()
		self.TotalHandValue = TotalHandValue

#keep pullng random card until you have one that hasnt been dealt using an if not equal to dealt card
#inside a for statement running through the dictionary of cards


#add a card to a current, ie HIT, also call it twice in the original hand dealing
	def add_card(self, Deck1):
		print 'add card routine start'
		#while self.TotalHandValue <= 21:
		  while UserDecision == "H":
				HitCard = Deck1.deal_one_card()
				ValueHitCard = ValueDict[HitCard[0]]
				print HitCard
				self.PlayerHand.append(HitCard)
				print self.PlayerHand
				self.TotalHandValue = self.TotalHandValue + ValueHitCard
				self.ace_count()
				self.display_hand_value()

				if self.TotalHandValue == 21:
					print "Perfect"
				elif self.TotalHandValue > 21:
					print 'BUST'
				elif self.five_card_charlie():



		  if UserDecision == 'S':
				if self.TotalHandValue == 21:
					print "Perfect"
				elif self.TotalHandValue > 21:
					print 'BUST'
				else:
					print 'You decided to stand with ', self.TotalHandValue
