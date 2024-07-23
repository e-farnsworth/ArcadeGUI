# Overview

The goal of this program is to apply a GUI using [Python Arcade](https://api.arcade.academy/en/latest/index.html) to a set of card tricks doable on the computer. You can run all of the basic python code for the three tricks is in the folder [CardTricks](CardTricks).

To play the GUI version, run [MainGame](MainGame.py). It will display a menu that will allow you to choose which trick you would like to play. Each trick will then display instructions for you to follow. The input for this game is conected solely to the mouse.

The three tricks that are in this program are ones where the user mentally selects a card from a list and the magician, or computer in this case, performs a series of moves in order to deduce which card the user has chosen. For more details on how each of the three tricks works, expand the details section below. 

Warning: the **Details** section explains how ALL of these *magic* tricks work, so only expand that section if you want to know the truth behind the magic.

<details>

<summary>Details</summary>

Important note, the names that I call these tricks may not be the names of the official trick. All of these card tricks can easily be done with actual cards though. The easiest ones are the 27 cards "filter" trick and the 21 cards trick. The tricks are laid out in order as they appear in the code.

### Trick 1: 27 Cards "Filter"

In the basic code, this trick is reffered to as [Card27Filter](CardTricks\Card27Filter.py)

This trick requires 27 random cards from the deck. Deal the cards out into three stacks of 9 and ask the audiance to select one in their mind. Then ask them which row or column their card is in. When restacking the cards, you may stack them in any order; however, it is important to remember if "their" stack is on the top, the bottom, or in the middle. This will determin which area you look at as you narrow down which card is theirs. 

To reveal their card, the easiest way is to point it out and veriify that that is their card. There is not fancy count off for this one.

To give a clearer picture of this trick, the following tables will represent the three stacks of cards. The "card" we are tracking will be noted by an **X** and all other "cards" will be noted by a **1**, **2**, or **3** depeding on their origianl pile. The potential cards will be bolded for convinence.

#### Deal 1

For this example, the actual card will start in stack 2

| First Stack | Seccond Stack | Third Stack |
| :---------: | :-----------: | :---------: |
| 1 | **2** | 3 |
| 1 | **2** | 3 |
| 1 | **2** | 3 |
| 1 | **2** | 3 |
| 1 | **2** | 3 |
| 1 | **2** | 3 |
| 1 | **X** | 3 |
| 1 | **2** | 3 |
| 1 | **2** | 3 |

#### Deal 2

The card has moved to the first stack, limiting the cards we're interested in

| First Stack | Seccond Stack | Third Stack |
| :---------: | :-----------: | :---------: |
| 1 | 1 | 1 |
| 1 | 1 | 1 |
| 1 | 1 | 1 |
| **2** | 2 | 2 |
| **2** | 2 | 2 |
| **X** | 2 | 2 |
| 3 | 3 | 3 |
| 3 | 3 | 3 |
| 3 | 3 | 3 |

#### Deal 3

The card is now in the third stack and we know which one it is.

| First Stack | Seccond Stack | Third Stack |
| :---------: | :-----------: | :---------: |
| 1 | 1 | 1 |
| 2 | 2 | **X** |
| 3 | 3 | 3 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |

### Trick 2: 21 Cards

In the basic code, this trick is reffered to as [Card21Min](CardTricks\Card21Mid.py).

This trick requires 21 random cards from the deck. Deal the cards out into three stacks of 7 and ask the audiance to select one in their mind. Then ask them which row or column their card is in. As you pick up the stacks, make sure to put the stack with their card in the middle. Re-deal the cards to the three stacks of 7 and ask which row or column their card is in again. Again, make sure to put the stack with their card in the middle. Do this action once more. After this third time of dealing, asking, and stacking, their card should be in the 11th position. 

To reveal their card, the easiest way would be to count off 11 cards, flipping the 11th and veriify that that is their card. 

The following link is the video that I referenced to code this trick. It is important to note that my code only covers the first half of this trick. [21 Cards Magic Trick](https://www.youtube.com/watch?v=_RS79RionDU&t=176s)

### Trick 3: 27 Cards "Number"

In the basic code, this trick is reffered to as [Card27Number](CardTricks\Card27Number.py).

This trick required 27 random cards from the deck and the memoriztion of the table shown below. While you *can* reference it, doing so will likely take away from some of the mystery. Before theis trick, ask the audiance what their favorite number is between 1 and 27. Based on the table below, you will place the stack with their card for each of the three deals and stacks.

This trick works very similar to the "filter" 27 cards trick, except the order that the cards are stacked matters. Depending on which card they chose, you stack the group with their card as follows durring each of the three deals.

| Number | First Stack | Seccond Stack | Third Stack |
| :----: | :---------: | :-----------: | :---------: |
| 1 | TOP | TOP | TOP |
| 2 | MIDDLE | TOP | TOP |
| 3 | BOTTOM | TOP | TOP |
| 4 | TOP | MIDDLE | TOP |
| 5 | MIDDLE | MIDDLE | TOP |
| 6 | BOTTOM | MIDDLE | TOP |
| 7 | TOP | BOTTOM | TOP |
| 8 | MIDDLE | BOTTOM | TOP |
| 9 | BOTTOM | BOTTOM | TOP |
| 10 | TOP | TOP | MIDDLE |
| 11 | MIDDLE | TOP | MIDDLE |
| 12 | BOTTOM | TOP | MIDDLE |
| 13 | TOP | MIDDLE | MIDDLE |
| 14 | MIDDLE | MIDDLE | MIDDLE |
| 15 | BOTTOM | MIDDLE | MIDDLE |
| 16 | TOP | BOTTOM | MIDDLE |
| 17 | MIDDLE | BOTTOM | MIDDLE |
| 18 | BOTTOM | BOTTOM | MIDDLE |
| 19 | TOP | TOP | BOTTOM |
| 20 | MIDDLE | TOP | BOTTOM |
| 21 | BOTTOM | TOP | BOTTOM |
| 22 | TOP | MIDDLE | BOTTOM |
| 23 | MIDDLE | MIDDLE | BOTTOM |
| 24 | BOTTOM | MIDDLE | BOTTOM |
| 25 | TOP | BOTTOM | BOTTOM |
| 26 | MIDDLE | BOTTOM | BOTTOM |
| 27 | BOTTOM | BOTTOM | BOTTOM |

To reveal their card, count off the cards until you reach their favorite number. Flip the card and veriify that that is their card.

The following link is the video that I referenced to code this trick. [27 Not 21 BRILLIANT Card Trick Tutorial](https://www.youtube.com/watch?v=gcgvFTfOpD8&t=186s)

</details>

<br/>

Admittedly, the main purpose of this program is to have fun providing a GUI for card tricks that are doable on the computer. Though this program has lead me to learn more about Arcade and about the problems that arise when atempting to apply a GUI onto code. It certainly is not as easy as it might sound.


[Software Demo Video](https://youtu.be/M6jtnFSskG0)

# Development Environment

Working Environment

- Python 3.10.11
- Python Arcade
- Visual Studio
- Git and GitHub

# Useful Websites

* [Solitaire Tutorial - Python Arcade](https://api.arcade.academy/en/latest/tutorials/card_game/index.html#shuffle-the-cards)
* [Drawing Text - Python Arcade](https://api.arcade.academy/en/latest/examples/drawing_text.html#drawing-text)
* [solitaire_09.py Full Listing](https://api.arcade.academy/en/latest/tutorials/card_game/solitaire_09.html#solitaire-09)
* [previous project - GameFramework](https://github.com/e-farnsworth/GameFramework)

Note: Other websites that I found useful when working with Python Arcade are listed under "Useful Wesites" in my **GameFramework** repository [README](https://github.com/e-farnsworth/GameFramework/blob/main/README.md)

# Future Work

* Get the third trick to work properly. Something is currently wrong with the stacking or the dealing
* Adding more tricks that work in this "filtering" way