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

class Choose27NumView(arcade.View):
    def __init__(self):
        super().__init__()

        self.multi_player = False

        # a UIManager to handle the UI
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Background color
        arcade.set_background_color(arcade.color.JUNGLE_GREEN)

        # Level Set slider
        ui_level_slider = UISlider(value=1, min_value=1, max_value=27, width=300, height=50)
        label = arcade.gui.UILabel(text= f"Favorite Number (1-27): {int(ui_level_slider.value)}")

        @ui_level_slider.event()
        def on_change(event: UIOnChangeEvent):
            label.text = f"Favorite Number (1-27): {int(ui_level_slider.value)}"
            label.fit_content()

        self.manager.add(arcade.gui.UIAnchorWidget(child=ui_level_slider))
        self.manager.add(arcade.gui.UIAnchorWidget(child=label,align_y=100))

        # Setting uniform button width
        BUTTON_WIDTH = 200

        #Creat a horizontile Boxgroup to align buttons
        self.h_box = arcade.gui.UIBoxLayout(vertical=False)

        ui_27num_button = arcade.gui.UIFlatButton(text="To Trick", width=BUTTON_WIDTH)
        self.h_box.add(ui_27num_button.with_space_around(bottom=20))

        # Handle Clicks
        @ui_27num_button.event("on_click")
        def on_click_ui_27num_button(event):
            num27 = Number27View(int(ui_level_slider.value))
            num27.setup()
            self.window.show_view(num27)
    
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="bottom", child = self.h_box))
        
    def on_draw(self):
        self.clear()
        self.manager.draw()

