import fib

#class fib(object):
#    def __init__(self):
#        self.last_1 = 1
#        self.last_2 = 1

#    def __iter__(self):	
#        return self

#    def next(self):
#        next_fib = self.last_1 + self.last_2
#        self.last_1, self.last2 = self.last_2, next_fib
#        return next_fib


def test1():
    f = fib.fib()
    assert f.next() == 2

def test2():
    f = fib.fib()
    f.next()
    assert f.next() == 3

def test3():
    f = fib.fib()
    f.next()
    f.next()
    assert f.next() == 5

test1()
test2()
test3()

