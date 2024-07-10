from Stack3CardTricks import Stack3CardTricks

class Card27Number(Stack3CardTricks):
    '''
    This one is a basic version of the 27 card trick that simply tracks and narrows down the possible cards the user could have picked
    '''   

    def __init__(self):
        self.stack_order = None
        self.number = None

    def favorite_number(self):
        answer_valid = False
        while answer_valid != True:
            self.number = input('What is your favorie number between 1 and 27? ')

            if self.number == '1':
                answer_valid = True
                self.stack_order = ['Top','Top','Top']
            elif self.number == '2':
                answer_valid = True
                self.stack_order = ['Mid','Top','Top']
            elif self.number == '3':
                answer_valid = True
                self.stack_order = ['End','Top','Top']
            elif self.number == '4':
                answer_valid = True
                self.stack_order = ['Top','Mid','Top']
            elif self.number == '5':
                answer_valid = True
                self.stack_order = ['Mid','Mid','Top']
            elif self.number == '6':
                answer_valid = True
                self.stack_order = ['End','Mid','Top']
            elif self.number == '7':
                answer_valid = True
                self.stack_order = ['Top','End','Top']
            elif self.number == '8':
                answer_valid = True
                self.stack_order = ['Mid','End','Top']
            elif self.number == '9':
                answer_valid = True
                self.stack_order = ['End','End','Top']
            elif self.number == '10':
                answer_valid = True
                self.stack_order = ['Top','Top','Mid']
            elif self.number == '11':
                answer_valid = True
                self.stack_order = ['Mid','Top','Mid']
            elif self.number == '12':
                answer_valid = True
                self.stack_order = ['End','Top','Mid']
            elif self.number == '13':
                answer_valid = True
                self.stack_order = ['Top','Mid','Mid']
            elif self.number == '14':
                answer_valid = True
                self.stack_order = ['Mid','Mid','Mid']
            elif self.number == '15':
                answer_valid = True
                self.stack_order = ['End','Mid','Mid']
            elif self.number == '16':
                answer_valid = True
                self.stack_order = ['Top','End','Mid']
            elif self.number == '17':
                answer_valid = True
                self.stack_order = ['Mid','End','Mid']
            elif self.number == '18':
                answer_valid = True
                self.stack_order = ['End','End','Mid']
            elif self.number == '19':
                answer_valid = True
                self.stack_order = ['Top','Top','End']
            elif self.number == '20':
                answer_valid = True
                self.stack_order = ['Mid','Top','End']
            elif self.number == '21':
                answer_valid = True
                self.stack_order = ['End','Top','End']
            elif self.number == '22':
                answer_valid = True
                self.stack_order = ['Top','Mid','End']
            elif self.number == '23':
                answer_valid = True
                self.stack_order = ['Mid','Mid','End']
            elif self.number == '24':
                answer_valid = True
                self.stack_order = ['End','Mid','End']
            elif self.number == '25':
                answer_valid = True
                self.stack_order = ['Top','End','End']
            elif self.number == '26':
                answer_valid = True
                self.stack_order = ['Mid','End','End']
            elif self.number == '27':
                answer_valid = True
                self.stack_order = ['End','End','End']
            else:
                print('That wasn\'t a valid answer.')
                   
    def findcard(self, list_of_cards, stack_index):
        '''
        Input the list of card lists and the index of the stack the user's card is in

        This function is the brains behind this card trick

        Returns the reordered list of lists to make the trick work
        '''
        new_stack_list = []
        # Take the next position the users stack needs to be in
        position = self.stack_order.pop(0)
        # Take the desired stack out so we don't acidentally do something we don't want
        stack = list_of_cards.pop(stack_index)

        if position == 'Top':
            new_stack_list.append(stack)
            other_stack = list_of_cards.pop(0)
            new_stack_list.append(other_stack)
            other_stack = list_of_cards.pop(0)
            new_stack_list.append(other_stack)

        elif position == 'Mid':
            other_stack = list_of_cards.pop(0)
            new_stack_list.append(other_stack)
            new_stack_list.append(stack)
            other_stack = list_of_cards.pop(0)
            new_stack_list.append(other_stack)

        else: # only other option is 'End'
            other_stack = list_of_cards.pop(0)
            new_stack_list.append(other_stack)
            other_stack = list_of_cards.pop(0)
            new_stack_list.append(other_stack)
            new_stack_list.append(stack)

        return new_stack_list
        
    def runtrick(self, deck):
        # Now we run the trick
        # We ask for a number between 1-27. This will be used later on
        self.favorite_number()
        # Shuffle the cards
        deck = self.shuffle(deck)

        print('For this magic trick, you will select a card from the cards shown.')
        print('Remember which card it is. You will select which stack it is in.')
        print('By the end, we will be able to tell you the card that you choose.')

        # the next steps need to be run three times in order to "reveal" the card
        for i in range(3):
            # deal the cards into the tree piles
            card_lists = self.deal(deck)
            # get the user to select a card and tell us which stack it is in
            possible_stack = self.choosestack(card_lists)
            # restack the list of lists in the order we want
            card_lists = self.findcard(card_lists, possible_stack)
            # restack the cards to be redelt
            deck = self.restack(card_lists)

        # their card should be in the number position they chose at the begining
        # to get some of the effect that we would get from in person, we count the cards out for the reveal
        for i in range(int(self.number)):
            card = deck.pop(0)
            print(f'{i+1}. {card}')
        
        print(f'Your card was the {card}')