from Card27Filter import Card27Filter
from Card27Number import Card27Number
from Card21Mid import Card21Mid

# List representing a stadard deck of 52 cards
deck_of_cards = ['As','2s','3s','4s','5s','6s','7s','8s','9s','10s','Js','Qs','Ks',
                'Ac','2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc',
                'Ah','2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh',
                'Ad','2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd']

def main27filter(deck_of_cards):
    basic27cards = Card27Filter()
    basic27cards.runtrick(deck_of_cards)

def main27number(deck_of_cards):
    advanced27cards = Card27Number()
    advanced27cards.runtrick(deck_of_cards)

def main21mid(dec_of_cards):
    mid21cards = Card21Mid()
    mid21cards.runtrick(deck_of_cards)

# Note: I have had problems in past running both 27 cards tricks one right after another

# main27number(deck_of_cards)

main27filter(deck_of_cards)

# main21mid(deck_of_cards)