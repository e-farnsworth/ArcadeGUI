import random

class Stack3CardTricks():
    '''
    This is all the common functions needed to do card tricks that require three stacks of cards
    '''
    
    def shuffle(self, deck_of_cards):
        '''
        Input is a list of cards of any positive length

        This shuffles the cards

        Return the randomized list
        '''
        # Create a location for our shuffled deck
        shuffled_deck = []

        for i in range(len(deck_of_cards)):
            # Select a random index within the original deck and remove it
            random_index = random.randint(0,len(deck_of_cards)-1)
            card = deck_of_cards.pop(random_index)
            # Add it to the new deck
            shuffled_deck.append(card)
        
        return shuffled_deck
    
    def deal(self, deck_of_cards):
        '''
        Input is a list of cards of any length equal to or greater then 27

        This function deals the deck into three equal lists of 9 cards

        Return the three lists in a list 
        '''
        # First we create our three card groups
        stack1 = []
        stack2 = []
        stack3 = []
        # Each group needs 9 cards "dealt" into it
        for i in range(9):
            # Take the front card 
            card = deck_of_cards.pop(0)
            # Add it to the first group
            stack1.append(card)
            # Take the front card
            card = deck_of_cards.pop(0)
            # Add it to the second group
            stack2.append(card)
            # Take the front card
            card = deck_of_cards.pop(0)
            # Add it to the third group
            stack3.append(card)

        return [stack1, stack2, stack3]

    def choosestack(self, stack_list):
        ''' 
        Input the list card lists from the "deal" function
        
        This function prints the lists and asks the user which stack their card is in
        
        Return the stack index that the card is in
        '''
        # list the stacks for choosing
        print(f'1. {stack_list[0]}')
        print(f'2. {stack_list[1]}')
        print(f'3. {stack_list[2]}')
        # int the input then subtract 1 to match up with python index
        stack_index = int(input('\nWhich stack is your card in? '))-1
        print()

        return stack_index
    
    def restack(self, list_of_cards):
        '''
        Input the list card lists from the "deal" function
        
        This function reformats the lists back into one list for the "deal" function

        Return a single list of cards
        '''
        # Create a group for our resulting deck
        deck = []
        # For each of the three "stacks" in the list of cards
        for stack in list_of_cards: 
            # We're going to extract the card and add it to the deck
            for card in stack:
                deck.append(card)
        # The double loop is fine since we are dealing with a finite number of cards.

        return deck

    def findcard(self):
        '''
        Each Subclass has different ways of finding or revealing the card.
        '''
        # This is a placeholder function
        pass

    def runtrick(self):
        '''
        This is the equivilent to a "main" function
        '''
        # This is a placeholder function
        pass
