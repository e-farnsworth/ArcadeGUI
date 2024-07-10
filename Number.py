import arcade

# Constants for sizing
NUMBER_SCALE = 1

# Each number has a width and height of 75 pixels
NUMBER_WAH = 75 * NUMBER_SCALE  

class Number(arcade.Sprite):
    """ Card sprite """

    def __init__(self, image_file_name, scale=1):
        """ Card constructor """
        # Call the parent
        super().__init__(image_file_name, scale)