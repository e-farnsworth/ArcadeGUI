from Stack3CardTricks import Stack3CardTricks

class Card27Filter(Stack3CardTricks): 
    '''
    This one is a basic version of the 27 card trick that simply tracks and narrows down the possible cards the user could have picked
    '''   
    
    def __init__(self):
        self.possible_card = None
    
    def findcard(self, card_stacks, stack_index):
        '''
        Input the stack that the user's card is in

        This function is the brains behind this card trick

        Sets self.possible_card each time is called
        '''
        card_stack = card_stacks[stack_index]
        if self.possible_card == None:
            # if this is the first round, set the possible card
            self.possible_card = card_stack
        else:
            # if this is not the first round, compare the new stack to the possible cards and find the cards in the intersection
            new_stack = []
            for card in card_stack:
                if card in self.possible_card:
                    new_stack.append(card)

            # reset the possible card to the intersection cards 
            self.possible_card = new_stack

    def runtrick(self, deck):
        # Now we run the trick
        # Shuffle the cards
        deck = self.shuffle(deck)

        # Tell the user what to expect and what is needed of them
        print('For this magic trick, you will select a card from the cards shown.')
        print('Remember which card it is. You will select which stack it is in.')
        print('By the end, we will be able to tell you the card that you choose.')

        # the next steps need to be run three times in order to "reveal" the card
        for i in range(3):
            # deal the cards into the tree piles
            card_lists = self.deal(deck)
            # get the user to select a card and tell us which stack it is in
            stack_index = self.choosestack(card_lists)
            # set the possible cards
            self.findcard(card_lists, stack_index)
            # restack the cards to be redelt
            deck = self.restack(card_lists)
        # And we give the grand reveal
        print(f'Your card was the {self.possible_card[0]}')
