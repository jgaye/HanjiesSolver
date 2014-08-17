from enum import IntEnum

class Box(IntEnum):
    """
    A Box is an object that have one of these three status: unknown (-1), white (0), black (1).
    It is initiated to unknown and can be then filled to white or black once.
    Once it has been filled, it can't change status anymore.
    A Box is printed as a ? (unknown), a □ (white) or a ■ (black).
    """
    unknown = -1
    white = 0
    black = 1


    #Init to unknown

    def __init__(self):
        self = unknown

    #Status setters

    def fill_white(self):
        if self.is_unknown():
            self = white
        else:
            print "This Box has already been filled"

    def fill_black(self):
        if self.is_unknown:
            self = 1
        else:
            print "This Box has already been filled"

    #Status getters

    def is_unknown(self):
        if self == unknown:
            return True
        else :
            return False

    def is_white(self):
        if self == white:
            return True
        else:
            return False

    def is_black(self):
        if self == black:
            return True
        else:
            return False

    #Representation

    def __repr__(self):
        if self.is_unknown:
            return "?"
        else if self.is_white:
            return u"\u25A1"
        else:
            return u"\u25A0"
