from Stack3CardTricks import Stack3CardTricks

class Card21Mid(Stack3CardTricks):
    
    def deal(self, deck_of_cards):
        '''
        Input is a list of cards of any length equal to or greater then 21

        This function deals the deck into three equal lists of 7 cards

        Return the three lists in a list 
        '''
        # First we create our three card groups
        stack1 = []
        stack2 = []
        stack3 = []
        # Each group needs 9 cards "dealt" into it
        for i in range(7):
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

    def findcard(self, list_of_cards, stack_index):
        '''
        Input the list of card lists and the index of the stack the user's card is in

        This function is the brains behind this card trick

        Returns the reordered list of lists to make the trick work
        '''
        new_stack_list = []
        # Take the next position the users stack needs to be in
        # Take the desired stack out so we don't acidentally do something we don't want
        stack = list_of_cards.pop(stack_index)

        # This trick requires us to put it in the middle each time
        other_stack = list_of_cards.pop(0)
        new_stack_list.append(other_stack)
        new_stack_list.append(stack)
        other_stack = list_of_cards.pop(0)
        new_stack_list.append(other_stack)

        return new_stack_list

    def runtrick(self, deck):
        # Now we run the trick
        # Shuffle the cardss
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
            # restack the list of lists in the order we want
            card_lists = self.findcard(card_lists, stack_index)
            # restack the cards to be redelt
            deck = self.restack(card_lists)

        # Their card should be in the 11th position
        print(f'Your card was the {deck[10]}')

