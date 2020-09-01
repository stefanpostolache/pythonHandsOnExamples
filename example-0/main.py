import random

"""
Module containing functions to create a hand of cards
"""

def createHand(handsize):
    """
    Creates a hand of cards

    Args:
        handsize (int): size of the hand of cards

    Returns:
        tuple: hand and remainder of the deck
    """
    deck = generateDeck()
    deck = shuffle(deck)
    return deal(deck,handsize)


def generateDeck():
    """Generates a deck

    Returns:
        list: deck of cards
    """
    deck = []

    values = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
    suits = ["hearts","diamonds","spades","clubs"]

    for value in values:
        for suit in suits:
            deck.append(value+" of "+suit)

    return deck


def shuffle(deck):
    """Shuffles a deck of cards

    Args:
        deck (list): deck of cards

    Returns:
        list: shuffled deck of cards
    """
    random.shuffle(deck)
    return deck


def deal(deck,handsize):
    """
    Separates a hand from the rest of the deck

    Args:
        deck (list): deck of cards
        handsize (int): how many cards should a hand have

    Returns:
        tuple: hand and remainder of deck
    """
    return (deck[:handsize],deck[handsize:])


def contains(deck,card):
    """[summary]

    Args:
        deck ([type]): [description]
        card ([type]): [description]

    Returns:
        [type]: [description]
    """
    return card in deck


