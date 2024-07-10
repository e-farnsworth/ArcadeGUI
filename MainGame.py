import arcade

from MenuView import MenuView

# Screen Information
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Magic Trick"

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()