import arcade
import random
import os
import arcade.gui
import arcade.csscolor
from arcade.experimental.uislider import UISlider
from arcade.gui.events import UIOnChangeEvent
from Card import Card
import random

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 750

# Constants for sizing
CARD_SCALE = 0.7

# How big are the cards?
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE

# How big is the mat we'll place each stack on
# we'll leave some overlap, 
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)
MAT_EDGE = int(MAT_WIDTH - CARD_WIDTH)

# Want three evenly spaced large mats
BOTTOM_Y = (SCREEN_HEIGHT/4) -10
MID_Y = (SCREEN_HEIGHT/2) -10
TOP_Y = (3*SCREEN_HEIGHT/4) -10

# X position to start putting mats and cards
X_POS9 = (SCREEN_WIDTH/2) - (4*(MAT_WIDTH-MAT_EDGE))
X_POS7 = (SCREEN_WIDTH/2) - (3*(MAT_WIDTH-MAT_EDGE))
X_POS = (SCREEN_WIDTH/2)

# Constants that represent "what pile is what" for the game
FULL_LIST = 0
TOP_STACK = 1
MIDDLE_STACK = 2
BOTTOM_STACK = 3

# Card constants
CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]

# Setting uniform button width
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40

# Text Properties
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

class Number27View(arcade.View):
    def __init__(self, fav_num):
        super().__init__()

        self.final_deal = False

        self.fav_num = fav_num
        self.number = str(fav_num)
        self.stack_order = None
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        #Creat a horizontile Boxgroup to align selection buttons
        self.h_box1 = arcade.gui.UIBoxLayout(vertical=False)

        ui_top_button = arcade.gui.UIFlatButton(text="TOP", width=BUTTON_WIDTH,height=BUTTON_HEIGHT)
        self.h_box1.add(ui_top_button.with_space_around(top=55))

        # Handle Clicks
        @ui_top_button.event("on_click")
        def on_click_ui_top_button(event):            
            cards = self.piles[TOP_STACK]

            if len(self.stack_order) == 0:
                self.reveal()
            else:
                self.redeal(TOP_STACK)
            
        ui_middle_button = arcade.gui.UIFlatButton(text="MIDDLE", width=BUTTON_WIDTH,height=BUTTON_HEIGHT)
        self.h_box1.add(ui_middle_button.with_space_around(top=55))

        # Handle Clicks
        @ui_middle_button.event("on_click")
        def on_click_ui_middle_button(event):            
            cards = self.piles[MIDDLE_STACK]

            if len(self.stack_order) == 0:
                self.reveal()
            else:
                self.redeal(MIDDLE_STACK)
            
        ui_bottom_button = arcade.gui.UIFlatButton(text="BOTTOM", width=BUTTON_WIDTH,height=BUTTON_HEIGHT)
        self.h_box1.add(ui_bottom_button.with_space_around(top=55))

        # Handle Clicks
        @ui_bottom_button.event("on_click")
        def on_click_ui_bottom_button(event):            
            cards = self.piles[BOTTOM_STACK]

            if len(self.stack_order) == 0:
                self.reveal()
            else:
                self.redeal(BOTTOM_STACK)
                
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="top", child = self.h_box1))
        
        #Creat a horizontile Boxgroup for back button
        self.h_box2 = arcade.gui.UIBoxLayout(vertical=False)

        ui_menu_button = arcade.gui.UIFlatButton(text="Back To Menu", width=BUTTON_WIDTH)
        self.h_box2.add(ui_menu_button.with_space_around(bottom=20))

        # Handle Clicks
        @ui_menu_button.event("on_click")
        def on_click_ui_menu_button(event):
            menu = MenuView()
            self.window.show_view(menu)

        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="bottom", child = self.h_box2))

        # Sprite list with all the cards, no matter what pile they are in.
        self.potential_card = None

        # Full Sprite lists
        self.card_list = None
        self.small_mat = None
        self.mat_list = None
        self.piles = None

        # set background color
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def setup(self):
        '''
        Game set up here. Call to restart
        '''
        # Sets up what order to stck the cards in
        if self.number == '1':
            self.stack_order = ['Top','Top','Top']
        elif self.number == '2':
            self.stack_order = ['Mid','Top','Top']
        elif self.number == '3':
            self.stack_order = ['End','Top','Top']
        elif self.number == '4':
            self.stack_order = ['Top','Mid','Top']
        elif self.number == '5':
            self.stack_order = ['Mid','Mid','Top']
        elif self.number == '6':
            self.stack_order = ['End','Mid','Top']
        elif self.number == '7':
            self.stack_order = ['Top','End','Top']
        elif self.number == '8':
            self.stack_order = ['Mid','End','Top']
        elif self.number == '9':
            self.stack_order = ['End','End','Top']
        elif self.number == '10':
            self.stack_order = ['Top','Top','Mid']
        elif self.number == '11':
            self.stack_order = ['Mid','Top','Mid']
        elif self.number == '12':
            self.stack_order = ['End','Top','Mid']
        elif self.number == '13':
            self.stack_order = ['Top','Mid','Mid']
        elif self.number == '14':
            self.stack_order = ['Mid','Mid','Mid']
        elif self.number == '15':
            self.stack_order = ['End','Mid','Mid']
        elif self.number == '16':
            self.stack_order = ['Top','End','Mid']
        elif self.number == '17':
            self.stack_order = ['Mid','End','Mid']
        elif self.number == '18':
            self.stack_order = ['End','End','Mid']
        elif self.number == '19':
            self.stack_order = ['Top','Top','End']
        elif self.number == '20':
            self.stack_order = ['Mid','Top','End']
        elif self.number == '21':
            self.stack_order = ['End','Top','End']
        elif self.number == '22':
            self.stack_order = ['Top','Mid','End']
        elif self.number == '23':
            self.stack_order = ['Mid','Mid','End']
        elif self.number == '24':
            self.stack_order = ['End','Mid','End']
        elif self.number == '25':
            self.stack_order = ['Top','End','End']
        elif self.number == '26':
            self.stack_order = ['Mid','End','End']
        elif self.number == '27':
            self.stack_order = ['End','End','End']


        # Sprite list with all the cards, no matter what pile they are in.
        self.card_list = arcade.SpriteList()
        self.potential_card = []

        # Sprite list with all mats the cards can lay on
        self.mat_list: arcade.SpriteList = arcade.SpriteList()

        # Mats will be overlapping
        for i in range(9):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.ROYAL_BLUE)
            pile.position = X_POS9 + i*(MAT_WIDTH-MAT_EDGE), BOTTOM_Y
            self.mat_list.append(pile)
            
        for i in range(9):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.ROYAL_BLUE)
            pile.position = X_POS9 + i*(MAT_WIDTH-MAT_EDGE), MID_Y
            self.mat_list.append(pile)
            
        for i in range(9):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.ROYAL_BLUE)
            pile.position = X_POS9 + i*(MAT_WIDTH-MAT_EDGE), TOP_Y
            self.mat_list.append(pile)

        # Create every card
        for card_suit in CARD_SUITS:
            for card_value in CARD_VALUES:
                card = Card(card_suit, card_value, CARD_SCALE)
                card.position = X_POS9, BOTTOM_Y # CARD POSITION
                self.card_list.append(card)

        # Shuffle the cards
        for pos1 in range(len(self.card_list)):
            pos2 = random.randrange(len(self.card_list))
            self.card_list.swap(pos1, pos2)

        # Get the correct number of cards for the trick
        while len(self.card_list) != 27:
            self.card_list.pop()

        # creates the number of lists in the listing that we need
        self.piles = [[] for _ in range(4)]

        # All cards in one pile for dealing
        for card in self.card_list:
            self.piles[FULL_LIST].append(card)

        # Deal amount to each pile
        for i in range(9):
            # get card from the full pile
            card = self.piles[FULL_LIST].pop(0)
            # fix position and pu into propper pile
            card.position = X_POS9 + i*(MAT_WIDTH-MAT_EDGE), TOP_Y
            self.piles[TOP_STACK].append(card)
            # get card from the full pile
            card = self.piles[FULL_LIST].pop(0)
            # put into propper pile
            card.position = X_POS9 + i*(MAT_WIDTH-MAT_EDGE), MID_Y
            self.piles[MIDDLE_STACK].append(card)
            # get card from the full pile
            card = self.piles[FULL_LIST].pop(0)
            # put into propper pile
            card.position = X_POS9 + i*(MAT_WIDTH-MAT_EDGE), BOTTOM_Y
            self.piles[BOTTOM_STACK].append(card)

    def on_draw(self):
        '''
        render the screen
        '''
        # clear the screen
        self.clear()

        # Draw Mats on the base
        self.mat_list.draw()

        # Draw numbers underneath the cards for reveal
        
        arcade.draw_text(f"1    2    3    4    5    6    7    8    9",
                            0,
                            TOP_Y,
                            arcade.color.BLACK,
                            DEFAULT_FONT_SIZE*2,
                            width=SCREEN_WIDTH,
                            align = "center"
                            )
            
        arcade.draw_text(f"10  11 12  13  14  15  16  17 18  19",
                            0,
                            MID_Y,
                            arcade.color.BLACK,
                            DEFAULT_FONT_SIZE*2,
                            width=SCREEN_WIDTH,
                            align = "center"
                            )
            
        arcade.draw_text(f"19   20  21  22  23  24  25  26   27",
                            0,
                            BOTTOM_Y,
                            arcade.color.BLACK,
                            DEFAULT_FONT_SIZE*2,
                            width=SCREEN_WIDTH,
                            align = "center"
                            )

        # Draw the cards
        self.card_list.draw()

        # Add instructions
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT
        arcade.draw_text("Select a card from the cards shown. Remember which card it is. Select which stack it is in.",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         width=SCREEN_WIDTH,
                         align="center")
        
        # Manager takes care of the drawing
        self.manager.draw()

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if self.final_deal == True:
            menu = MenuView()
            self.window.show_view(menu)

    def pull_to_top(self, card: arcade.Sprite):
        """ Pull card to top of rendering order (last to render, looks on-top) """

        # Remove, and append to the end
        self.card_list.remove(card)
        self.card_list.append(card)

    def redeal(self,chosen_index):
        # Restack the cards into one pile to be redealt
        position = self.stack_order.pop(0)
        index_list = [1,2,3]
        index_list.pop(chosen_index-1)

        if position == 'Top':
            for card in self.piles[chosen_index]:
                self.piles[FULL_LIST].append(card)
            for card in self.piles[index_list.pop(0)]:
                self.piles[FULL_LIST].append(card)
            for card in self.piles[index_list.pop(0)]:
                self.piles[FULL_LIST].append(card)

        elif position == 'Mid':
            for card in self.piles[index_list.pop(0)]:
                self.piles[FULL_LIST].append(card)
            for card in self.piles[chosen_index]:
                self.piles[FULL_LIST].append(card)
            for card in self.piles[index_list.pop(0)]:
                self.piles[FULL_LIST].append(card)

        else: # only other option is 'End'
            for card in self.piles[index_list.pop(0)]:
                self.piles[FULL_LIST].append(card)
            for card in self.piles[index_list.pop(0)]:
                self.piles[FULL_LIST].append(card)
            for card in self.piles[chosen_index]:
                self.piles[FULL_LIST].append(card)
    
        self.piles[TOP_STACK] = []
        self.piles[MIDDLE_STACK] = []
        self.piles[BOTTOM_STACK] = []

        # Deal amount to each pile
        for i in range(9):
            # get card from the full pile
            card = self.piles[FULL_LIST].pop(0)
            # fix position and pu into propper pile
            card.position = X_POS9 + i*(MAT_WIDTH-MAT_EDGE), TOP_Y
            self.piles[TOP_STACK].append(card)
            # get card from the full pile
            card = self.piles[FULL_LIST].pop(0)
            # put into propper pile
            card.position = X_POS9 + i*(MAT_WIDTH-MAT_EDGE), MID_Y
            self.piles[MIDDLE_STACK].append(card)
            # get card from the full pile
            card = self.piles[FULL_LIST].pop(0)
            # put into propper pile
            card.position = X_POS9 + i*(MAT_WIDTH-MAT_EDGE), BOTTOM_Y
            self.piles[BOTTOM_STACK].append(card)

    def reveal(self):
        if self.fav_num < 10:
            stack = self.piles[TOP_STACK]
            card = stack[self.fav_num - 1]
        elif self.fav_num > 18:
            stack = self.piles[BOTTOM_STACK]
            card = stack[self.fav_num - 1 - 18]
        else:
            stack = self.piles[MIDDLE_STACK]
            card = stack[self.fav_num - 1 - 9]
            
        self.pull_to_top(card)
        card.set_scale()
        card.position = X_POS, MID_Y
        self.final_deal=True
