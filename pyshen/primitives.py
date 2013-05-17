# primitives.py ---
import numpy
from pyshen.core import PartialDecorator, Sym, SException

################################################################################
################################   PRIMITIVES   ################################
################################################################################

def shen_cons_str(f):
    if isinstance(f, list):
        return '(' + " ".join([shen_cons_str(x) for x in f]) + ")"
    else:
        return str(f)

def shen_to_cons(array):
    if len(array) == 0:
        return []
    else:
        index = len(array) - 1
        head = [array[index], []]
        index = index - 1
        while index >= 0:
            head = [array[index], head]
            index -= 1
        return head

def shen_cons_iter(cons):
    cell = cons
    while not cell == []:
        yield car(cell)
        cell = cdr(cell)

def car(cons):
    return [] if cons == [] else cons[0]

def cdr(cons):
    if cons.__class__ is list:
        return [] if (cons == [] or len(cons) < 2) else cons[1]
    else:
        raise SException("%s is not a list" %str(cons))

def cons_nth(n, lst):
    return cons_nth(n - 1, cdr(lst)) if n > 0 else car(lst)

def cons_length(lst, count=0):
    tl = cdr(lst)
    if tl.__class__ is list and tl != []:
        return 1 + cons_length(tl)
    elif tl == []:
        return 1
    else:
        return 2
    # return cons_length(cdr(lst), count + 1) if lst else count

def shen_simple_error(msg):
    raise SException(msg)

def shen_try_except(success, failure):
    try:
        return success()
    except SException, e:
        return failure(e)

class AbsVector(numpy.ndarray):
    # def __init__(self, n):
        # numpy.ndarray.__init__(self, shape=n, dtype=object)
    def __eq__(self, other):
        if other.__class__ != AbsVector:
            return False
        if self is other:
            return True
        if len(self) != len(other):
            return False
        return numpy.equal(self, other).all()

def shen_absvector(n):
    if not isinstance(n, int):
        raise SException("%s is not a number" %str(n))
    if n < 0:
        raise SException("%d must be >= 0" %n)
    # vec = [Sym("shen.fail!")] * (n + 1)
    vec = AbsVector(n + 1, dtype=object)
    vec[:] = Sym("shen.fail!")
    return vec

def shen_absvector_set(vec, n, value):
    if not isinstance(vec, AbsVector):
        raise SException("%s is not a vector" %str(vec))
    if not isinstance(n, int):
        raise SException("%s is not a number" %str(n))
    if n < 0 or n >= len(vec):
        raise SException("%d out of bound" %n)
    vec[n] = value
    return vec

def shen_absvector_get(vec, n):
    # print "GET", vec, n, vec[n]
    if not isinstance(vec, AbsVector):
        raise SException("%s is not a vector" %str(vec))
    if not isinstance(n, int):
        raise SException("%s is not a number" %str(n))
    if n < 0 or n >= len(vec):
        raise SException("%d out of bound" %n)
    return vec[n]

def shen_absvectorp(vec):
    # return isinstance(vec, list)
    return isinstance(vec, AbsVector)

def shen_pr(s, stream):
    if stream == sys.stdin:
        stream = sys.stdout
    stream.write(s)
    return s

def shen_read_byte(stream):
    rd = stream.read(1)
    return ord(rd) if len(rd) > 0 else -1

def shen_open(stream_type, name, direction):
    # print "Opening", stream_type, name, direction, type(direction)
    if not stream_type.sym == "file":
        raise SException("unsupported stream type")
    return open(name, "w" if direction.sym == "out" else "r")

def shen_close(stream):
    stream.close()

def shen_get_time(mode):
    if mode.sym == "run":
        return time.time()
    elif mode.sym == "real":
        return time.time()
    else:
        raise SException("unsupported get-time mode %s" %mode.sym)

def shen_intern(s):
    return Sym(s)

def shen_consp(exp):
    if exp.__class__ is list and len(exp) > 0:
        return True
    return False

@PartialDecorator(2)
def shen_add(x, y):
    return x + y
@PartialDecorator(2)
def shen_sub(x, y): return x - y
@PartialDecorator(2)
def shen_mul(x, y): return x * y
@PartialDecorator(2)
def shen_div(x, y): return x / y

@PartialDecorator(2)
def shen_abseq(x, y):
    if shen_absvectorp(x) and shen_absvectorp(y):
        return numpy.equal(x, y).all()
    else:
        return x == y

@PartialDecorator(2)
def shen_eq(x, y):
    return x == y

@PartialDecorator(2)
def shen_gt(x, y): return x > y
@PartialDecorator(2)
def shen_lt(x, y): return x < y
@PartialDecorator(2)
def shen_gte(x, y): return x >= y
@PartialDecorator(2)
def shen_lte(x, y): return x <= y
@PartialDecorator(2)
def shen_or(x, y): return x or y
@PartialDecorator(2)
def shen_and(x, y): return x and y
