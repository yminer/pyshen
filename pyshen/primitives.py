# primitives.py ---
import numpy
import time
import sys
from pyshen.core import PartialDecorator, Sym, SException

################################################################################
################################   PRIMITIVES   ################################
################################################################################


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
