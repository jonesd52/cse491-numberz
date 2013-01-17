# this is an implementation of the 'series' functionality using
# Python's iterator functionality.  Here, 'adder' is a class that
# obeys the iterator protocol.

class adder(object):
    def __init__(self):     # creates instance of adder class
        self.n = 0          # sets the n value to 0 for 

    def __iter__(self):
        return self         # returns value of self

    def next(self):         # defines what happens when iterator happens
        self.n += 1         # ADD 1 to n
        return self.n
