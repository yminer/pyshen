# cons.py --- 

class Nil:
    def car(self):
        return nil
    def cdr(self):
        return nil
    def __repr__(self):
        return "()"
    def __iter__(self):
        return self
    def next(self):
        raise StopIteration
    def __len__(self):
        return 0

nil = Nil()
Nil.__init__ = None

class Cons:
    def __init__(self, hd, tl):
        self.hd = hd
        self.tl = tl
        if isinstance(tl, Cons):
            self.size = 1 + len(tl)
        elif tl is nil:
            self.size = 1
        else:
            self.size = 2

    def car(self):
        return self.hd

    def cdr(self):
        return self.tl

    def __len__(self):
        return self.size

    def __iter__(self):
        cell = self
        while not cell is nil:
            yield cell.car()
            cell = cell.cdr()

    def nth(self, index):
        i = 0
        for item in self:
            if i == index:
                return item
            i += 1
        raise IndexError

    def __repr__(self):
        return '(' + " ".join([str(x) for x in self]) + ")"

    def __eq__(self, other):
        if self is other:
            return True
        if not consp(other):
            return False
        if not len(other) == self.size:
            return False
        for a, b in zip(self, other):
            if not a == b:
                return False
        return True

def shen_cons_str(f):
    return str(f)

def shen_to_cons(array):
    ret = nil
    array.reverse()
    for item in array:
        ret = Cons(item, ret)
    return ret

def car(cons):
    return cons.car()

def cdr(cons):
    return cons.cdr()

def cons_nth(n, lst):
    return cons_nth(n - 1, cdr(lst)) if n > 0 else car(lst)

def cons_length(lst):
    return len(lst)

def consp(exp):
    return isinstance(exp, Cons)

shen_consp = consp
