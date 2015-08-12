from Deck import Deck

#move this to the main program later
def user_input():
	global UserDecision
	UserDecision = raw_input("Hit (H) or Stand (S)?   ")

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
		self.TotalHandValue = 0
		self.PlayerHand = []
		self.Charlie = False

#initial dealing of the hand, calls the AddCard method twice
	def deal_hand(self, Deck1):
		Card1 = Deck1.deal_one_card()
		Card2 = Deck1.deal_one_card()
		print Card1, Card2

		#initialize user input helper function
		user_input()

		self.PlayerHand = [Card1, Card2]

#helper method to figure out the value of aces in hand
	def ace_count(self):
		HighAce = False
		ValueFirstCard = ValueDict[self.PlayerHand[0][0]]
		ValueSecondCard = ValueDict[self.PlayerHand[1][0]]
		# print len(self.PlayerHand)
		# print UserDecision
		if len(self.PlayerHand) == 2 and UserDecision == "S":
			for card in self.PlayerHand:
				#If one ace in the initial hand, then it is always a high ace (11)
				if ValueFirstCard == 11 or ValueSecondCard == 11:
					HighAce = True
					#If two aces, set one to 1, no order required
					if ValueFirstCard == 11 and ValueSecondCard == 11:
						ValueFirstCard = 1


		#if total is more than 21, reduce all aces to 1
		else:
			if self.TotalHandValue > 21:
				for card in self.PlayerHand:
					number_of_aces = 0
					if ValueDict[card[0]] == 11:
						number_of_aces += 1
						print "I have ", number_of_aces, " Aces"
						HighAce = False
						self.TotalHandValue = self.TotalHandValue - 10
						print 'Aces have been reduced from 11 to 1 and you new hand value is', self.TotalHandValue
						first_aces_decision = raw_input("Hit (H) or Stand (S)?   ")
						print self.TotalHandValue
						if first_aces_decision == 'H' and self.TotalHandValue < 20:
							HighAce = True
							self.TotalhandValue = self.TotalHandValue + 10
							print 'It made sense to up one ace to 11'
						elif first_aces_decision == 'H' and self.TotalHandValue > 20:
							print 'AutoStand with ', self.TotalHandValue,' for Safety'

#conveniently display the status of a hand
	def display_hand_value(self):
		self.ace_count()
		TotalHandValue = 0
		for card in self.PlayerHand:
			self.TotalHandValue += ValueDict[card[0]]


#add a card to a current hand, ie HIT, also call it twice in the original hand dealing
	def add_card(self, Deck1):
		#while self.TotalHandValue <= 21:
		if UserDecision == "H":
			HitCard = Deck1.deal_one_card()
			ValueHitCard = ValueDict[HitCard[0]]
			print HitCard
			self.PlayerHand.append(HitCard)
			print "the new hand is ", self.PlayerHand
			self.TotalHandValue = self.TotalHandValue + ValueHitCard
			self.ace_count()

			if self.TotalHandValue == 21:
				print "Perfect"
			elif self.TotalHandValue > 21:
				print "BUST"
			elif self.TotalHandValue < 16:
				user_input()
				# self.ace_count()
			else:
				print 'AutoStand with ', self.TotalHandValue,' for Safety'


		elif UserDecision == 'S':
			if self.TotalHandValue == 21:
				print 'Perfect'
			elif self.TotalHandValue > 21:
				print 'BUST with ', self.TotalHandValue,
			else:
				print 'You decided to Stand with ', self.TotalHandValue
