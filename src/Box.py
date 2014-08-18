class Box(object):
    """
    A Box is an object that have one of these three status: unknown (-1), white (0), black (1).
    It is initiated to unknown and can be then filled to white or black once.
    Once it has been filled, it can't change status anymore.
    A Box is printed as a ? (unknown), a white square (white) or a black square (black).
    """
    #Init to unknown

    def __init__(self):
        self.status = -1

    #Status setters

    def fill_white(self):
        if self.is_unknown():
            self.status = 0
        else:
            print "This Box has already been filled"

    def fill_black(self):
        if self.is_unknown:
            self.status = 1
        else:
            print "This Box has already been filled"

    #Status getters

    def is_unknown(self):
        return self.status == -1

    def is_white(self):
        return self.status == 0

    def is_black(self):
        return self.status == 1

    #Representation

    def __repr__(self):
        if self.is_unknown:
            return "?"
        elif self.is_white:
            return u"\u25A1"
        else:
            return u"\u25A0"
