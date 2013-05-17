#  -*- Mode: Python -*- 
import os
import sys
import re
import numbers
import ast
import StringIO
import copy
import itertools
import numpy
import unparse
import types
import collections
import contextlib
import functools
import threading
import inspect
import time
import uuid

################################################################################
################################   ENVIRONMENT   ###############################
################################################################################

sys.setrecursionlimit(10000)

FUNCTIONS = dict()
FUNARITIES = dict()
VARS = dict()
SYMS = ['!', '}', '{', '-->', '<--', '&&', ':', ';', ':-', ':=', '_', '*language*', '*implementation*', '*stinput*', '*home-directory*', '*version*', '*maximum-print-sequence-size*', '*macros*', '*os*', '*release*', '*property-vector*', '@v', '@p', '@s', '*port*', '*porters*', '<-', '->', '<e>', '==', '=', '>=', '>', '/.', '=!', '$', '-', '/', '*', '+', '<=', '<', '>>', '==>', 'y-or-n?', 'write-to-file', 'where', 'when', 'warn', 'version', 'verified', 'variable?', 'value', 'vector->', '<-vector', 'vector', 'vector?', 'unspecialise', 'untrack', 'unit', 'shen.unix', 'union', 'unify', 'unify!', 'unprofile', 'undefmacro', 'return', 'type', 'tuple?', "false", 'trap-error', 'track', 'time', 'thaw', 'tc?', 'tc', 'tl', 'tlstr', 'tlv', 'tail', 'systemf', 'synonyms', 'symbol', 'symbol?', 'string->symbol', 'subst', 'string?', 'string->n', 'stream', 'string', 'stinput', 'stoutput', 'step', 'spy', 'specialise', 'snd', 'simple-error', 'set', 'save', 'str', 'run', 'reverse', 'remove', 'read', 'read-file', 'read-file-as-bytelist', 'read-file-as-string', 'read-byte', 'read-from-string', 'quit', 'put', 'preclude', 'preclude-all-but', 'ps', 'prolog?', 'protect', 'profile-results', 'profile', 'print', 'pr', 'pos', 'package', 'output', 'out', 'or', 'open', 'occurrences', 'occurs-check', 'n->string', 'number?', 'number', 'null', 'nth', 'not', 'nl', 'mode', 'macro', 'macroexpand', 'maxinferences', 'mapcan', 'map', 'make-string', 'load', 'loaded', 'list', 'lineread', 'limit', 'length', 'let', 'lazy', 'lambda', 'is', 'intersection', 'inferences', 'intern', 'integer?', 'input', 'input+', 'include', 'include-all-but', 'in', 'if', 'identical', 'head', 'hd', 'hdv', 'hdstr', 'hash', 'get', 'get-time', 'gensym', 'function', 'fst', 'freeze', 'fix', 'file', 'fail', 'fail-if', 'fwhen', 'findall', "true", 'enable-type-theory', 'explode', 'external', 'exception', 'eval-kl', 'eval', 'error-to-string', 'error', 'empty?', 'element?', 'do', 'difference', 'destroy', 'defun', 'define', 'defmacro', 'defcc', 'defprolog', 'declare', 'datatype', 'cut', 'cn', 'cons?', 'cons', 'cond', 'concat', 'compile', 'cd', 'cases', 'call', 'close', 'bind', 'bound?', 'boolean?', 'boolean', 'bar!', 'assoc', 'arity', 'append', 'and', 'adjoin', '<-address', 'address->', 'absvector?', 'absvector', 'abort', "super", "exists", "assert", "for", "while"]
SYMDIC = dict()
SYMDIC_MODE = False

class PartialDecorator:
    def __init__(self, arity):
        self.arity = arity

    def __call__(self, func):
        def partial_wrapper(*FUN_ARGS):
            if len(FUN_ARGS) < self.arity:
                return lambda *args: apply(partial_wrapper, FUN_ARGS + args)
            return apply(func, FUN_ARGS)
        return partial_wrapper

class Singleton:
    """ A python singleton """

    class __impl:
        """ Implementation of the singleton interface """

        def spam(self):
            """ Test method, return singleton id """
            return id(self)

    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if Singleton.__instance is None:
            # Create and remember instance
            Singleton.__instance = Singleton.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = Singleton.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)

class Sym(ast.Name):
    sym = ""
    value = None
    lineno = 1
    def __init__(self, sym):
        # sym = sym.replace("-", "_").replace(".", "x").replace(">", "_").replace("<", "_").replace("?", "_P").replace("*", "_")
        def pystr(s):
            matcher = re.compile("[a-zA-Z0-9_]")
            news = ""
            for ch in s:
                if ch == ".":
                    news += "_"
                elif not matcher.match(ch):
                    news += "x%d" %ord(ch)
                else:
                    news += ch
            return news
        self.sym = intern(sym)
        if self.sym in SYMS:
            self.ssym = "kl_" + pystr(self.sym)
        else:
            self.ssym = pystr(self.sym)
        # "kl_" + str(slugify(unicode(self.sym.replace(".", "_")))).replace("-", "_")
        self.value = None
    def __repr__(self):
        return self.sym
    def value(self):
        if self.value == None:
            raise SException("variable " + self.sym + " has no value")
        return self.value
    def __eq__(self, other):
        return (other is self) or (isinstance(other, Sym) and self.sym == other.sym)
    def hashcode(self):
        h = 0
        for c in self.sym:
            h = (31 * h + ord(c)) & 0xFFFFFFFF
        return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000
    def slug(self):
        return self.ssym
    def nodeSym(self):
        global SYMDIC, SYMDIC_MODE
        if SYMDIC_MODE:
            if not self.sym in SYMDIC:
                SYMDIC[self.sym] = "symdic_" + self.ssym
            return ast.Attribute(value=ast.Name(id="symdic", ctx=ast.Load()),
                                 attr=SYMDIC[self.sym],
                                 ctx=ast.Load())
        else:
            return ast.fix_missing_locations(ast.Call(func=ast.Name(id="Sym", ctx=ast.Load()),
                                                      keywords=[], starargs=None, kwargs=None,
                                                      args=[ast.Str(self.sym, lineno=1)],
                                                      lineno=1))
    def nodeName(self):
        return ast.Name(id=self.ssym, ctx=ast.Load())
    @staticmethod
    def new(self, sym):
        return Sym(sym)

class SymTrue(Sym, Singleton):
    def __init__(self):
        Sym.__init__("true")
    def nodeSym(self):
        return ast.Name(id="True", ctx=ast.Load())

class SymFalse(Sym, Singleton):
    def __init__(self):
        Sym.sym = intern("false")
    def nodeSym(self):
        return ast.Name(id="False", ctx=ast.Load())

ShenTrue = Sym("true")
ShenFalse = Sym("false")

class SException(Exception):
    pass


################################################################################
################################   PRIMITIVES   ################################
################################################################################

def tail_call(fun, args):
    global tramp_fn, tramp_args
    tramp_fn, tramp_args = fun, args
    # return None#[tramp_fn, tramp_args]

def tco_apply(fun, args, glob=globals()):
    global tramp_fn, tramp_args
    while fun != None:
        tramp_fn = None
        if fun.__class__ == Sym:
            fun = shen_get_fun(fun.sym)
        result = apply(fun, args)
        # try:
        #     arity = fun.arity
        # except AttributeError, e:
        #     # print FUNARITIES
        #     # arity = FUNARITIES[fun]
        #     arity = len(inspect.getargspec(fun).args)
        #     fun.arity = arity
        # argsize = len(args)
        # if arity == argsize or arity == 0:
        #     result = apply(fun, args)
        # elif arity > argsize:
        #     result = functools.partial(fun, *args)
        #     result.arity = arity - argsize
        # else:
        #     raise SException("not handled yet")
        if tramp_fn:
            args = tramp_args
            tramp_args = None
            fun = tramp_fn
        else:
            fun = None
    return result

def tail_recursion(func):
    return func

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

def pyshen_set(s, value):
    s.value = value
    return v

def set_local(s, value):
    # print sys._getframe(1).f_locals, sys._getframe(1).f_locals[s]
    sys._getframe(1).f_locals[s] = value
    return value

def get_local(s):
    return sys._getframe(1).f_locals[s]

@PartialDecorator(2)
def shen_set(sym, value):
    global VARS
    VARS[sym.sym] = value
    return value

def shen_get(sym):
    global VARS
    try:
        return VARS[sym.sym]
    except Exception, e:
        raise SException(e.message)

def shen_apply(sym, args, glob=globals()):
    global FUNCTIONS
    if isinstance(sym, Sym):
        return tco_apply(shen_get_fun(sym.sym), args, glob)
    else:
        return tco_apply(sym, args, glob)

def shen_add_fun(name, fun, arity=None, glob=globals()):
    global FUNCTIONS, FUNARITIES
    FUNCTIONS[intern(name)] = fun
    return Sym(name)

def shen_get_fun(name):
    global FUNCTIONS
    try:
        return FUNCTIONS[name]
    except Exception, e:
        raise SException(e.message)

def shen_compile(form, rvalue=False):
    env = ShenEnv()
    code = env.compile_shen(form)
    # print ast.dump(code)
    module = ast.Module(body=[])
    if isinstance(code, list):
        for line in code:
            module.body.append(line)
    else:
        module.body.append(code)
    ShenVisitorLocals().visit(module)
    ShenVisitorUnlambda().visit(module)
    ShenVisitorApply().visit(module)
    ShenVisitor().visit(module)
    ShenVisitorPartial().visit(module)
    if rvalue:
        if not isinstance(module.body[-1], ast.FunctionDef):
            last = module.body[-1]
            module.body[-1] = ast.Assign(targets=[ast.Name(id="result", ctx=ast.Store())],
                                       value=last)
    fix(module)
    # print ast.dump(module,include_attributes=True)
    return module

def shen_eval_kl(form, glob=globals()):
    global tramp_fn, tramp_args
    # print "Initial form", form
    code = shen_compile(form, True)
    # io = StringIO.StringIO()
    # unparse.Unparser(code, io)
    # io.write("\n")
    # print "IO", io.getvalue()#, glob.keys()
    tramp_fn = None
    try:
        bcode = compile(code, "<string>", "exec")
        exec(bcode, glob)#, ldict)
    except Exception, e:
        io = StringIO.StringIO()
        unparse.Unparser(code, io)
        io.write("\n")
        print "Error ", e.message, io.getvalue()
        print ast.dump(code)
        raise e
    # print ldict
    if tramp_fn != None:
        fun = tramp_fn
        args = tramp_args
        tramp_fn, tramp_args = None, None
        return shen_apply(fun, args, glob)
    else:
        # print "Returning", ldict['result']
        return glob['result']


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

################################################################################
################################   PARSER   ####################################
################################################################################

fix = ast.fix_missing_locations

def ast_expr(val):
    return val

class Lexer:
    SYMBOL_CHARS = "[-=*\/+_?$!\@~><&%'#`;:{}a-zA-Z0-9.]"

    class OpenPar(Singleton):
        pass

    class ClosePar(Singleton):
        pass

    def __init__(self, stream):
        self.stream = stream
        self.buffer = []
        self.eof = False
        self.re_ws = re.compile("\S")
        self.re_d = re.compile("\d")
        self.re_sym = re.compile(self.SYMBOL_CHARS)
        self.re_sgn = re.compile("[+-]")

    def __iter__(self):
        return self

    def eofp(self):
        return len(self.buffer) == 0 and self.eof

    def getc(self):
        if len(self.buffer) == 0:
            c = self.stream.read(1)
            if not c:
                self.eof = True
                return None
            return c
        else:
            return self.buffer.pop(0)

    def ungetc(self, c):
        self.buffer.append(c)

    def next(self):
        self.whitespaces()
        if not self.eofp():
            c = self.getc()
            if c == '(':
                return self.OpenPar()
            elif c == ')':
                return self.ClosePar()
            elif c == '"':
                return self.consume_string()
            elif self.re_sym.match(c):
                self.ungetc(c)
                return self.consume_num_or_sym()
            else:
                raise SException("illegal character: %d" %(ord(c)))

    def whitespaces(self):
        while True:
            c = self.getc()
            if self.eofp():
                break
            if self.re_ws.match(c):
                self.ungetc(c)
                break

    def consume_string(self):
        chars = []
        while True:
            if self.eofp():
                raise SException("unterminated string")
            c = self.getc()
            if c == '"':
                break
            chars.append(c)
        return ''.join(chars)

    def consume_num(self):
            decimal_seen, negative, past_sign = False, False, False
            chars = []
            while True:
                c = self.getc()
                if self.eofp():
                    break
                if self.re_d.match(c):
                    past_sign = True
                    chars += c
                elif c == '.' and not decimal_seen:
                    past_sign = True
                    decimal_seen = True
                    chars += c
                elif c == '+' and not past_sign:
                    pass
                elif c == '-' and not past_sign:
                    negative = not negative
                else:
                    self.ungetc(c)
                    break
            if negative:
                chars.insert(0, '-')
            if chars[-1] == '.':
                self.ungetc(chars.pop(0))
                decimal_seen = False
            strb = ''.join(chars)
            if decimal_seen:
                return float(strb)
            else:
                return int(strb)

    def consume_sym(self):
        global ShenTrue, ShenFalse
        chars = []
        while True:
            c = self.getc()
            if self.eofp():
                break
            if not self.re_sym.match(c):
                self.ungetc(c)
                break
            chars += c
        strb = ''.join(chars)
        if strb == "true":
            return ShenTrue
        elif strb == "false":
            return ShenFalse
        else:
            return Sym(strb)

    def consume_num_or_sym(self):
            chars = []
            while True:
                c = self.getc()
                if self.eofp():
                    break
                if not self.re_sgn.match(c):
                    self.ungetc(c)
                    break
                chars += c
            if self.eofp():
                # chars.reverse()
                for c in chars:
                    self.ungetc(c)
                return self.consume_sym()
            c = self.getc()
            chars += c
            if c == '.':
                if self.eofp():
                    # chars.reverse()
                    for c in chars:
                        self.ungetc(c)
                    return self.consume_sym()
                c = self.getc()
                chars += c
                # chars.reverse()
                for c in chars:
                    self.ungetc(c)
                if self.re_d.match(c):
                    return self.consume_num()
                else:
                    return self.consume_sym()
            elif self.re_d.match(c):
                # chars.reverse()
                for c in chars:
                    self.ungetc(c)
                return self.consume_num()
            else:
                # chars.reverse()
                for c in chars:
                    self.ungetc(c)
                return self.consume_sym()

def shen_reader(stream):
    lexer = Lexer(stream)
    def read_list():
        items = []
        stack = [items]
        while len(stack) > 0:
            token = lexer.next()
            # print token
            if token == None:
                raise SException("unterminated list")
            if isinstance(token, Lexer.OpenPar):
                items = []
                stack.append(items)
            elif isinstance(token, Lexer.ClosePar):
                lst = shen_to_cons(stack.pop())
                # print "LIST          +++", lst
                if len(stack) > 0:
                    items = stack[-1]
                    items.append(lst)
            else:
                items.append(token)
        return lst
    while True:
        token = lexer.next()
        if token != None:
            if isinstance(token, Lexer.OpenPar):
                yield read_list()
            else:
                yield token
        else:
            break

################################################################################
################################   COMPILER   ##################################
################################################################################

class ShenVisitorPartial(ast.NodeTransformer):
    # def visit_Lambda(self, node):
    #     saved = self.localfuns
    #     self.localfuns = []
    #     self.generic_visit(node)
    #     body = []
    #     for fun in self.localfuns:
    #         body.append(fun)
    #     if isinstance(node.body, list):
    #         body += node.body
    #     else:
    #         body.append(node.body)
    #     body[-1] = ast.Return(body[-1])
    #     node = ast.FunctionDef(name=self.gensym(),
    #                            args=ast.arguments(args=[node.args], defaults=[], vararg=None, kwarg=None),
    #                            body=body, decorator_list=[])
    #     self.localfuns = saved
    #     self.localfuns.append(node)
    #     return ast.Name(id=node.name, ctx=ast.Load())
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        arguments = node.args
        fun_arity = ast.Assign(targets=[ast.Name(id="FUN_ARITY", ctx=ast.Store())],
                               value=ast.Num(n=len(arguments.args)))
        partial_test = ast.parse("if len(FUN_ARGS) < FUN_ARITY: return lambda *lambdaargs: apply(%s, FUN_ARGS + lambdaargs)"
                                 %node.name)
        partial_test.lineno = 1
        partial_test.col_offset = 0
        fix(partial_test)
        # print ast.dump(partial_test)
        body = [fun_arity] + partial_test.body
        count = 0
        for arg in node.args.args:
            body.append(ast.Assign(targets=[ast.Name(id=arg.id, ctx=ast.Store())],
                                   value=ast.Subscript(value=ast.Name(id="FUN_ARGS", ctx=ast.Load()),
                                                       slice=ast.Index(value=ast.Num(n=count)),
                                                       ctx=ast.Load())))
            count += 1
        node.body = body + node.body
        node.args.args = []
        node.args.vararg = "FUN_ARGS"
        return node

class ShenVisitorUnlambda(ast.NodeTransformer):
    localfuns = []
    count = 0
    def gensym(self):
        self.count += 1
        return "fun_%d" %self.count
    def visit_Call(self, node):
        # if node.func.id=="apply" and isinstance(node.args[0], ast.Lambda):
        #     self.generic_visit(node)
        #     if not isinstance(node.args[0], ast.FunctionDef):
        #         raise SException("ast transforamtion failed " + node.args)
        #     fun = node.args[0]
        #     node.args[0] = ast.Name(id=fun.name, ctx=ast.Load())
        #     return node
        self.generic_visit(node)
        return node
    # def visit_Lambda(self, node):
    #     saved = self.localfuns
    #     self.localfuns = []
    #     self.generic_visit(node)
    #     body = []
    #     for fun in self.localfuns:
    #         body.append(fun)
    #     if isinstance(node.body, list):
    #         body += node.body
    #     else:
    #         body.append(node.body)
    #     body[-1] = ast.Return(body[-1])
    #     node = ast.FunctionDef(name=self.gensym(),
    #                            args=ast.arguments(args=[node.args], defaults=[], vararg=None, kwarg=None),
    #                            body=body, decorator_list=[])
    #     self.localfuns = saved
    #     self.localfuns.append(node)
    #     return ast.Name(id=node.name, ctx=ast.Load())
    def visit_FunctionDef(self, node):
        savedloc = self.localfuns
        self.localfuns = []
        self.generic_visit(node)
        nbody = []
        nloc = min(2, node.nlocals)
        for fun in self.localfuns:
            nbody.append(fun)
        # print "LOCFUN", self.localfuns
        for line in range(len(node.body)):
            if line < nloc:
                nbody.insert(line, node.body[line])
            else:
                nbody.append(node.body[line])
        # nbody += node.body
        nbody[-1] = ast.Return(nbody[-1])
        node.body = nbody
        self.localfuns = savedloc
        return node

class ShenVisitorApply(ast.NodeTransformer):
    def visit_Call(self, node):
        # print ast.dump(node)
        self.generic_visit(node)
        if isinstance(node.func, ast.Name) and (node.func.id=="apply" or node.func.id == "tail_call" or node.func.id == "tco_apply") and isinstance(node.args[0], Sym):
            # print node
            fun = node.args[0]
            node.args[0] = ast.Name(id=fun.slug(), ctx=ast.Load())
            return node
        elif isinstance(node.func, ast.Name) and (node.func.id=="apply" or node.func.id == "tail_call" or node.func.id == "tco_apply") and isinstance(node.args[0], ast.Name) and node.args[0].id.startswith("KL_"):
            # print node
            node.func.id = "shen_apply"
            return node
        return node
    # def visit_Assign(self, node):
    #     self.generic_visit(node)
    #     # return node
    #     if node.visited == False:
    #         return ast.Call(func=ast.Name(id='setattr', ctx=ast.Load()),
    #                     keywords=[], starargs=None, kwargs=None,
    #                     args=[ast.Name(id="KL_CTX", ctx=ast.Load()),
    #                           ast.Str(s=node.targets[0].id),
    #                           node.value])
    #     else:
    #         return node


class ShenVisitorLocals(ast.NodeTransformer):
    localvars = []
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.localvars.append(node)
        return node
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id=="setattr" and len(node.args) == 3 and isinstance(node.args[0], ast.Name) and node.args[0].id == "KL_CTX":
            self.localvars.append(ast.Name(id=node.args[1].s, ctx=ast.Store()))
        self.generic_visit(node)
        return node
    def visit_FunctionDef(self, node):
        savedloc = self.localvars
        self.localvars = []
        self.generic_visit(node)
        nbody = []
        for var in self.localvars:
            nbody.append(ast.Assign(targets=[var], value=ast.Name(id="None", ctx=ast.Load()), visited=True))
        node.nlocals = len(self.localvars)
        if node.nlocals > 0:
            cdef = ast.ClassDef(name="KL_Context", bases=[], keyword=None, startargs=None, kwargs=None, decorator_list=[],
                                body = nbody)
            node.body = [cdef, ast.Assign(targets=[ast.Name(id="KL_CTX", ctx=ast.Store())],
                                          visited=True,
                                          value=ast.Call(func=ast.Name(id="KL_Context", ctx=ast.Load()),
                                                         keywords=[], starargs=None, kwargs=None,
                                                         args=[]))] + node.body
        self.localvars = savedloc
        return node
    def visit_Module(self, node):
        self.localvars = []
        self.generic_visit(node)
        nbody = []
        for var in self.localvars:
            nbody.append(ast.Assign(targets=[var], value=ast.Name(id="None", ctx=ast.Load()), visited=True))
        node.nlocals = len(self.localvars)
        if node.nlocals > 0:
            classname = "KL_Context_%s" %uuid.uuid1()
            cdef = ast.ClassDef(name=classname, bases=[], keyword=None, startargs=None, kwargs=None, decorator_list=[],
                                body = nbody)
            node.body = [cdef, ast.Assign(targets=[ast.Name(id="KL_CTX", ctx=ast.Store())],
                                          visited=True,
                                          value=ast.Call(func=ast.Name(id=classname, ctx=ast.Load()),
                                                         keywords=[], starargs=None, kwargs=None,
                                                         args=[]))] + node.body
        return node

class ShenVisitor(ast.NodeTransformer):
    def visit_Sym(self, node):
        return node.nodeSym()


class ShenEnv:
    PRIMITIVES = {
        'pr': (2, lambda s, stream: ast_expr(ast.Call(func=ast.Name(id='shen_pr', ctx=ast.Load()),
                                                      keywords=[], starargs=None, kwargs=None,
                                                      args=[s, stream])),
               ast.Name(id='shen_pr', ctx=ast.Load())),
        'read-byte': (1, lambda stream: ast_expr(ast.Call(func=ast.Name(id='shen_read_byte', ctx=ast.Load()),
                                                          keywords=[], starargs=None, kwargs=None,
                                                          args=[stream])),
                      ast.Name(id='shen_read_byte', ctx=ast.Load())),
        'open': (3, lambda stream_type, name, direction: ast_expr(ast.Call(func=ast.Name(id='shen_open', ctx=ast.Load()),
                                                                           keywords=[], starargs=None, kwargs=None,
                                                                           args=[stream_type, name, direction])),
                 ast.Name(id='shen_open', ctx=ast.Load())),
        'close': (1, lambda stream: ast_expr(ast.Call(func=ast.Name(id='shen_close', ctx=ast.Load()),
                                                      keywords=[], starargs=None, kwargs=None,
                                                      args=[stream])),
                  ast.Name(id='shen_close', ctx=ast.Load())),
        'get-time': (1, lambda x: ast_expr(ast.Call(func=ast.Name(id='shen_get_time', ctx=ast.Load()),
                                                    keywords=[], starargs=None, kwargs=None,
                                                    args=[x])),
                     ast.Name(id='shen_get_time', ctx=ast.Load())),
        '+': (2, lambda x, y: ast.BinOp(x, ast.Add(), y),
              ast.Name(id='shen_add', ctx=ast.Load())),
        '-': (2, lambda x, y: ast_expr(ast.BinOp(x, ast.Sub(), y)),
              ast.Name(id='shen_sub', ctx=ast.Load())),
        '*': (2, lambda x, y: ast_expr(ast.BinOp(x, ast.Mult(), y)),
              ast.Name(id='shen_mul', ctx=ast.Load())),
        '/': (2, lambda x, y: ast_expr(ast.BinOp(x, ast.Div(), y)),
              ast.Name(id='shen_div', ctx=ast.Load())),
        '>': (2, lambda x, y: ast_expr(ast.Compare(left=x, ops=[ast.Gt()], comparators=[y])),
              ast.Name(id='shen_gt', ctx=ast.Load())),
        '<': (2, lambda x, y: ast_expr(ast.Compare(left=x, ops=[ast.Lt()], comparators=[y])),
              ast.Name(id='shen_lt', ctx=ast.Load())),
        '>=': (2, lambda x, y: ast_expr(ast.Compare(left=x, ops=[ast.GtE()], comparators=[y])),
               ast.Name(id='shen_gte', ctx=ast.Load())),
        '<=': (2, lambda x, y: ast_expr(ast.Compare(left=x, ops=[ast.LtE()], comparators=[y])),
               ast.Name(id='shen_lte', ctx=ast.Load())),
        'number?': (1, lambda x: ast_expr(ast.Call(func=ast.Name(id='isinstance', ctx=ast.Load()),
                                                   keywords=[], starargs=None, kwargs=None,
                                                   args=[x, ast.Attribute(value=ast.Name(id="numbers", ctx=ast.Load()),
                                                                          attr="Number",
                                                                          ctx=ast.Load())])),
                    ast.Name(id='shen_numberp', ctx=ast.Load())),
        'set': (2, lambda x, y: ast_expr(ast.Call(func=ast.Name(id="shen_set", ctx=ast.Load()),
                                                  keywords=[], starargs=None, kwargs=None,
                                                  args=[x, y])),
                ast.Name(id="shen_set", ctx=ast.Load())),
        # 'set': (2, lambda x, y: ast_expr(ast.Assign(targets=[x], value=y))),
        'value': (1, lambda x: ast_expr(ast.Call(func=ast.Name(id="shen_get", ctx=ast.Load()),
                                                  keywords=[], starargs=None, kwargs=None,
                                                  args=[x])),
                  ast.Name(id='shen_value', ctx=ast.Load())),
        'or': (2, lambda x, y: ast_expr(ast.BoolOp(op=ast.Or(), values=[x, y])),
               ast.Name(id='shen_or', ctx=ast.Load())),
        'and': (2, lambda x, y: ast_expr(ast.BoolOp(op=ast.And(), values=[x, y])),
                ast.Name(id='shen_and', ctx=ast.Load())),
        'not': (1, lambda x: ast_expr(ast.UnaryOp(op=ast.Not(), operand=x)),
                ast.Name(id='shen_not', ctx=ast.Load())),
        'simple-error': (1, lambda x: ast_expr(ast.Call(func=ast.Name(id='shen_simple_error', ctx=ast.Load()),
                                                        keywords=[], starargs=None, kwargs=None,
                                                        args=[x])),
                         ast.Name(id='shen_simple_error', ctx=ast.Load())),
        'error-to-string': (1, lambda x: ast_expr(ast.Attribute(value=x,
                                                                attr="message",
                                                                ctx=ast.Load())),
                            ast.Name(id='shen_error_to_string', ctx=ast.Load())),
        # 'if': (3, lambda x, y, z: ast_expr(ast.IfExp(x, y, z))),
        'hd': (1, lambda x: ast_expr(ast.Subscript(value=x,
                                                   slice=ast.Index(value=ast.Num(n=0)),
                                                   ctx=ast.Load())),
               ast.Name(id='shen_hd', ctx=ast.Load())),
        'tl': (1, lambda x: ast_expr(ast.Subscript(value=x,
                                                   slice=ast.Index(value=ast.Num(n=1)),
                                                   ctx=ast.Load())),
               ast.Name(id='shen_tl', ctx=ast.Load())),
        'intern': (1, lambda x: ast_expr(ast.Call(func=ast.Name(id='shen_intern', ctx=ast.Load()),
                                                  keywords=[], starargs=None, kwargs=None,
                                                  args=[x]))),
        'pos': (2, lambda s, n: ast_expr(ast.Subscript(value=s,
                                                       slice=ast.Index(value=n),
                                                       ctx=ast.Load()))),
        'tlstr': (1, lambda s: ast_expr(ast.Subscript(value=s,
                                                      slice=ast.Slice(lower=ast.Num(n=1), upper=None, step=None),
                                                      ctx=ast.Load()))),
        'cn': (2, lambda x, y: ast_expr(ast.BinOp(x, ast.Add(), y))),
        'str': (1, lambda x: ast_expr(ast.Call(func=ast.Name(id='str', ctx=ast.Load()),
                                               keywords=[], starargs=None, kwargs=None,
                                               args=[x]))),
        'string?': (1, lambda x: ast_expr(ast.Call(func=ast.Name(id='isinstance', ctx=ast.Load()),
                                                   keywords=[], starargs=None, kwargs=None,
                                                   args=[x, ast.Name(id="str", ctx=ast.Load())]))),
        'n->string': (1, lambda x: ast_expr(ast.Call(func=ast.Name(id='chr', ctx=ast.Load()),
                                                     keywords=[], starargs=None, kwargs=None,
                                                     args=[x]))),
        'string->n': (1, lambda x: ast_expr(ast.Call(func=ast.Name(id='ord', ctx=ast.Load()),
                                                     keywords=[], starargs=None, kwargs=None,
                                                     args=[x]))),
        '=': (2, lambda x, y: ast.Call(func=ast.Name(id='shen_eq', ctx=ast.Load()),
                                                     keywords=[], starargs=None, kwargs=None,
                                                     args=[x, y]),
              ast.Name(id='shen_eq', ctx=ast.Load())),
        'absvector': (1, lambda n: ast_expr(ast.Call(func=ast.Name(id='shen_absvector', ctx=ast.Load()),
                                                     keywords=[], starargs=None, kwargs=None,
                                                     args=[x]))),
        'absvector': (1, lambda n: ast_expr(ast.Call(func=ast.Name(id='shen_absvector', ctx=ast.Load()),
                                                     keywords=[], starargs=None, kwargs=None,
                                                     args=[n]))),
        'address->': (3, lambda v, n, val: ast_expr(ast.Call(func=ast.Name(id='shen_absvector_set', ctx=ast.Load()),
                                                             keywords=[], starargs=None, kwargs=None,
                                                             args=[v, n, val]))),
        '<-address': (2, lambda v, n: ast_expr(ast.Call(func=ast.Name(id='shen_absvector_get', ctx=ast.Load()),
                                                        keywords=[], starargs=None, kwargs=None,
                                                        args=[v, n]))),
        'absvector?': (1, lambda v: ast_expr(ast.Call(func=ast.Name(id='shen_absvectorp', ctx=ast.Load()),
                                                      keywords=[], starargs=None, kwargs=None,
                                                      args=[v]))),
        'eval-kl': (1, lambda v: ast_expr(ast.Call(func=ast.Name(id='shen_eval_kl', ctx=ast.Load()),
                                                      keywords=[], starargs=None, kwargs=None,
                                                      args=[v])))
    }

    def attributeNode(self, sym):
        if isinstance(sym, Sym):
            return ast.Name(id=sym.slug(), ctx=ast.Load())
        else:
            return ast.Name(id=sym, ctx=ast.Load())

    def compile_shen(self, form, lexical_vars = {}, in_tail_pos = True, **kwargs):
        if isinstance(form, SymTrue):
            return ast.Name(id='True', ctx=ast.Load())
        elif isinstance(form, SymFalse):
            return ast.Name(id='False', ctx=ast.Load())
        elif isinstance(form, Sym):
            if form.sym == "true":
                return ast.Name(id='True', ctx=ast.Load())
            elif form.sym == "false":
                return ast.Name(id='False', ctx=ast.Load())
            if form.sym in lexical_vars:
                name = lexical_vars[form.sym]
                if name.startswith("KL_LOC"):
                    return ast.Attribute(value=ast.Name(id="KL_CTX", ctx=ast.Load()),
                                         attr=name, ctx=ast.Load())
                else:
                    return ast.Name(id=name, ctx=ast.Load())
            else:
                return form
        elif isinstance(form, str):
            return ast.Str(form)
        elif form == []:
            return ast.parse("[]", mode="eval").body
        elif isinstance(form, list):
            return self.compile_form(form, lexical_vars, in_tail_pos, **kwargs)
        elif isinstance(form, numbers.Number):
            return ast.Num(form)
        else:
            raise SException("unexpected form %s" %form)

    def compile_defun(self, form, lexical_vars):
        name, arglist, body = cons_nth(1, form), cons_nth(2, form), cons_nth(3, form)
        # print "defun", name, "ARG", arglist, "body", body
        if not isinstance(name, Sym):
            raise SException(name + " is not a symbol")
        if not (isinstance(arglist, list) or arglist == []):
            raise SException(name + " is not a list")
        for arg in shen_cons_iter(arglist):
            if not isinstance(arg, Sym):
                raise SException(arg + " is not a symbol")
        # if name.sym in self.PRIMITIVES:
            # raise SException(name.sym + " is a primitive and cannot be redefined")
        extended_vars = self.add_vars(lexical_vars, [arg for arg in shen_cons_iter(arglist)], prefix="KL_ARG")
        fn_name = name.slug()
        fn_args = [ast.Name(id=extended_vars[arg.sym], ctx=ast.Load()) for arg in shen_cons_iter(arglist)]
        fn_body = self.compile_shen(body, extended_vars, True)
        if not isinstance(fn_body, list):
            fn_body = [fn_body]
        fn_body.insert(0, ast.Global(["symdic"]))
        fun = ast.FunctionDef(name=fn_name, args=ast.arguments(args=fn_args, defaults=[], vararg=None, kwarg=None),
                              body=fn_body,
                              decorator_list=[ast.Name(id="tail_recursion", ctx=ast.Load())])
        return [fun, ast.Call(func=ast.Name(id="shen_add_fun", ctx=ast.Load()),
                              keywords=[], starargs=None, kwargs=None,
                              args=[ast.Str(s=name.sym),
                                    ast.Name(id=fn_name, ctx=ast.Load()),
                                    ast.Num(n=len(fn_args))])]

    def compile_lambda(self, form, lexical_vars):
        var, body = cons_nth(1, form), cons_nth(2, form)
        if not isinstance(var, Sym):
            raise SException(var + " is not a symbol")
        # print var, body, lexical_vars
        extended_vars = self.add_var(lexical_vars, var, prefix="KL_ARG")
        fn_args = ast.Name(id=extended_vars[var.sym], ctx=ast.Load())
        fn_body = self.compile_shen(body, extended_vars, True)
        if isinstance(fn_body, list):
            fn_body = ast.Subscript(value=ast.List(elts=fn_body, ctx=ast.Load()),
                                    slice=ast.Index(value=ast.Num(n=-1)),
                                    ctx=ast.Load())
        return ast.Lambda(ast.arguments(args=[fn_args], defaults=[], vararg=None, kwarg=None), fn_body)

    def compile_form(self, form, lexical_vars, in_tail_pos, **kwargs):
        hd = car(form)
        sym = hd.sym if isinstance(hd, Sym) else None
        # print "compile_form", form, sym
        expr = None
        if sym == "defun":
            expr = self.compile_defun(form, lexical_vars)
        elif sym == "lambda":
            expr = self.compile_lambda(form, lexical_vars)
        elif sym == "let":
            expr = self.compile_let(form, lexical_vars, in_tail_pos, **kwargs)
        elif sym == "freeze":
            expr = self.compile_freeze(form, lexical_vars, in_tail_pos)
        elif sym == "type":
            expr = self.compile_type(form, lexical_vars, in_tail_pos)
        elif sym == "if":
            expr = self.compile_if(form, lexical_vars, in_tail_pos)
        elif sym == "or":
            expr = self.compile_or(form, lexical_vars, in_tail_pos)
        elif sym == "and":
            expr = self.compile_and(form, lexical_vars, in_tail_pos)
        elif sym == "cond":
            expr = self.compile_cond(form, lexical_vars, in_tail_pos)
        elif sym == "do":
            expr = self.compile_do(form, lexical_vars, in_tail_pos)
        elif sym == "trap-error":
            expr = self.compile_trap_error(form, lexical_vars, in_tail_pos)
        elif sym == "cons":
            expr = self.compile_cons(form, lexical_vars, in_tail_pos)
        elif sym == "cons?":
            expr = self.compile_consp(form, lexical_vars, in_tail_pos)
        else:
            expr = self.compile_application(form, lexical_vars, in_tail_pos)
        self.parent_form = sym
        return expr

    def compile_cons(self, form, lexical_vars, in_tail_pos):
        if cons_length(form) == 3:
            hd, tl = cons_nth(1, form), cons_nth(2, form)
            hd_expr = self.compile_shen(hd, lexical_vars, False)
            tl_expr = self.compile_shen(tl, lexical_vars, False)
            return ast.List(elts=[hd_expr, tl_expr], ctx=ast.Load())
        else:
            return self.compile_application(form, lexical_vars, in_tail_pos)

    def compile_consp(self, form, lexical_vars, in_tail_pos):
         if cons_length(form) == 2:
             expr = self.compile_shen(car(cdr(form)), lexical_vars, False)
             return ast.Call(func=ast.Name(id='shen_consp', ctx=ast.Load()),
                             keywords=[], starargs=None, kwargs=None,
                             args=[expr])
         else:
             return self.compile_application(form, lexical_vars, in_tail_pos)

    def compile_trap_error(self, form, lexical_vars, in_tail_pos):
        expr, err_handler = cons_nth(1, form), cons_nth(2, form)
        # serr = Sym("err")
        try_body = self.compile_shen(expr, lexical_vars, False)
        try_clause = ast.Lambda(ast.arguments(args=[], defaults=[], vararg=None, kwarg=None), try_body)
        # extended_vars = self.add_var(lexical_vars, serr)
        # err_var = extended_vars[serr.sym]
        # catch_clause = self.compile_application(shen_to_cons([err_handler, serr]),
                                                # extended_vars, False)
        catch_clause = self.compile_shen(err_handler, lexical_vars, False)
        return ast.Call(func=ast.Name(id='shen_try_except', ctx=ast.Load()),
                        keywords=[], starargs=None, kwargs=None,
                        args=[try_clause, catch_clause])
        
    def compile_do(self, form, lexical_vars, in_tail_pos):
        if cons_length(form) == 3:
            expr1, expr2 = cons_nth(1, form), cons_nth(2, form)
            body1 = self.compile_shen(expr1, lexical_vars, False)
            body2 = self.compile_shen(expr2, lexical_vars, in_tail_pos)
            return ast.Subscript(value=ast.List(elts=[body1, body2], ctx=ast.Load()),
                                 slice=ast.Index(value=ast.Num(n=-1)),
                                 ctx=ast.Load())
        else:
            return self.compile_application(form, lexical_vars, in_tail_pos)

    def compile_if(self, form, lexical_vars, in_tail_pos):
        test_expr, true_expr, false_expr = cons_nth(1, form), cons_nth(2, form), cons_nth(3, form)
        test_clause = self.compile_shen(test_expr, lexical_vars, False)
        true_clause = self.compile_shen(true_expr, lexical_vars, in_tail_pos)
        false_clause = self.compile_shen(false_expr, lexical_vars, in_tail_pos)
        return ast.IfExp(test_clause, true_clause, false_clause)
    
    def compile_or(self, form, lexical_vars, in_tail_pos):
        global ShenTrue, ShenFalse
        if cons_length(form) == 3:
            exp1, exp2 = cons_nth(1, form), cons_nth(2, form)
            return self.compile_if(shen_to_cons([Sym("if"), exp1, ShenTrue, exp2]),
                                   lexical_vars, in_tail_pos)
        else:
            return self.compile_application(form, lexical_vars, in_tail_pos)
        
    def compile_and(self, form, lexical_vars, in_tail_pos):
        global ShenTrue, ShenFalse
        if cons_length(form) == 3:
            exp1, exp2 = cons_nth(1, form), cons_nth(2, form)
            return self.compile_if(shen_to_cons([Sym("if"), exp1, exp2, ShenFalse]),
                                   lexical_vars, in_tail_pos)
        else:
            return self.compile_application(form, lexical_vars, in_tail_pos)

    def compile_cond(self, form, lexical_vars, in_tail_pos):
        clauses = cdr(form)
        if clauses == []:
            return self.compile_shen(shen_to_cons([Sym("simple-error"), "condition failure"]))
        else:
            clause = car(clauses)
            test_expr = car(clause)
            true_expr = car(cdr(clause))
            false_expr = [Sym("cond"), cdr(clauses)]
            # print "FALSE", false_expr
            return self.compile_shen(shen_to_cons([Sym("if"), test_expr, true_expr, false_expr]),
                                     lexical_vars, in_tail_pos)

    def compile_type(self, form, lexical_vars, in_tail_pos):
        expr = cons_nth(2, form)
        return self.compile_shen(expr, lexical_vars, in_tail_pos)

    def compile_freeze(self, form, lexical_vars, in_tail_pos):
        # print "fsize", form.size, form
        if cons_length(form) == 2:
            expr = cons_nth(1, form)
            body = self.compile_shen(expr, lexical_vars, True)
            return ast.Lambda(ast.arguments(args=[], defaults=[], vararg=None, kwarg=None), body)
        else:
            return self.compile_application(form, lexical_vars, in_tail_pos)

    def compile_let2(self, form, lexical_vars, in_tail_pos, **kwargs):
        if "inlet" in kwargs and kwargs["inlet"]:
            return self.compile_let_lambda(form, lexical_vars, in_tail_pos)
        else:
            var, expr, body = cons_nth(1, form), cons_nth(2, form), cons_nth(3, form)
            assert(isinstance(var, Sym))
            # print"compile_let", var, expr, body, kwargs
            extended_vars = self.add_var(lexical_vars, var)
            bound_var = extended_vars[var.sym]
            args = dict(inlet=True)
            bound_expr = self.compile_shen(expr, lexical_vars, False, **args)
            let_body = self.compile_shen(body, extended_vars, in_tail_pos, **args)
            return [ast.Assign(targets=[ast.Name(id=bound_var, ctx=ast.Store())], value=bound_expr),
                    let_body]

    def compile_let(self, form, lexical_vars, in_tail_pos):
        var, expr, body = cons_nth(1, form), cons_nth(2, form), cons_nth(3, form)
        assert(isinstance(var, Sym))
        # print"compile_let", var, expr, body
        extended_vars = self.add_var(lexical_vars, var)
        bound_var = extended_vars[var.sym]
        bound_expr = self.compile_shen(expr, lexical_vars, False)
        let_body = self.compile_shen(body, extended_vars, in_tail_pos)
        return ast.Subscript(value=ast.List(elts=[#ast.Assign(targets=[ast.Name(id=bound_var, ctx=ast.Store())], value=bound_expr, visited=False),
                                                   ast.Call(func=ast.Name(id='setattr', ctx=ast.Load()),
                                                            keywords=[], starargs=None, kwargs=None,
                                                            args=[ast.Name(id="KL_CTX", ctx=ast.Load()), ast.Str(s=bound_var),
                                                                  bound_expr]),
                                                   let_body], ctx=ast.Load()),
                             slice=ast.Index(value=ast.Num(n=-1)),
                             ctx=ast.Load())

    def compile_let_lambda(self, form, lexical_vars, in_tail_pos):
        var, expr, body = cons_nth(1, form), cons_nth(2, form), cons_nth(3, form)
        assert(isinstance(var, Sym))
        # print"compile_let", var, expr, body
        extended_vars = self.add_var(lexical_vars, var)
        bound_var = extended_vars[var.sym]
        bound_expr = self.compile_shen(expr, lexical_vars, False)
        let_body = self.compile_shen(body, extended_vars, in_tail_pos)
        return ast.Call(func=ast.Name(id='apply', ctx=ast.Load()),
                        keywords=[], starargs=None, kwargs=None,
                        args=[ast.Lambda(ast.arguments(args=[ast.Name(id=bound_var, ctx=ast.Load())], defaults=[], vararg=None, kwarg=None), let_body),
                              ast.List(elts=[bound_expr], ctx=ast.Load())])

    def compile_application(self, form, lexical_vars, in_tail_pos):
        global SYMS
        f, args = car(form), cdr(form)
        # print "Application", form, lexical_vars, "ARGS", args, cons_length(args), in_tail_pos
        if isinstance(f, Sym) and intern(f.sym) in self.PRIMITIVES and cons_length(args) == self.PRIMITIVES[f.sym][0]:
            # print "PRIM", f.sym
            fargs = [self.compile_shen(arg, lexical_vars, False) for arg in shen_cons_iter(args)]
            return apply(self.PRIMITIVES[f.sym][1], fargs)
        else:
            # print "APP", f.sym
            if isinstance(f, Sym) and intern(f.sym) in self.PRIMITIVES:
                rator = self.PRIMITIVES[f.sym]
                if len(rator) == 3:
                    rator = rator[2]
                else:
                    raise SException("primitive %s not available on partial" %f.sym)
            else:
                rator = self.compile_shen(f, lexical_vars, False)
            # if isinstance(rator, Sym):
                # rator = rator.nodeSym()
            rands = [self.compile_shen(arg, lexical_vars, False) for arg in shen_cons_iter(args)]
            if isinstance(rator, Sym) and rator.sym in ["declare"]:
                return ast.Call(func=ast.Name(id="apply", ctx=ast.Load()),
                                keywords=[], starargs=None, kwargs=None,
                                args=[rator, ast.List(elts=rands, ctx=ast.Load())])
            elif in_tail_pos:
                return ast.Call(func=ast.Name(id="tail_call", ctx=ast.Load()),
                                keywords=[], starargs=None, kwargs=None,
                                args=[rator, ast.List(elts=rands, ctx=ast.Load())])
            else:
                return ast.Call(func=ast.Name(id="tco_apply", ctx=ast.Load()),
                                keywords=[], starargs=None, kwargs=None,
                                args=[rator, ast.List(elts=rands, ctx=ast.Load())])

    def add_var(self, scope, var, prefix="KL_LOC"):
        return self.add_vars(scope, [var], prefix=prefix)

    def add_vars(self, scope, vars, prefix="KL_LOC"):
        new_scope = copy.copy(scope)
        for var in vars:
            new_scope[var.sym] = self.gensym(prefix + "_" + var.ssym)
        return new_scope


    counter = 0

    def gensym (self, name="KL_LOC"):
        r = '%s_%d' % (name, self.counter)
        self.counter += 1
        return r

    def __init__(self):
        self.dump_code = True
        self.VARIABLES = {}
        self.FUNCTIONS = dict()


    def value(self, sym):
        return self.VARIABLES[sym].value

    def eval(self, form):
        # if self.dump_code:
        #     print "=" * 70
        #     print "Compiling", shen_cons_str(form)
        #     print "-----"
        code = self.compile_shen(form, {}, True)
        if not isinstance(code, ast.Str):
            if not isinstance(code, list):
                code = [code]
            for c in code:
                ShenVisitorLocals().visit(c)
                ShenVisitorUnlambda().visit(c)
                ShenVisitorApply().visit(c)
                ShenVisitor().visit(c)
                ShenVisitorPartial().visit(c)
                fix(c)
                yield c

    def getDeclarations(self, decls=[], postdecls=[]):
        decls = decls + self.DECLS + postdecls
        init = ast.FunctionDef(name="shen_init",
                               args=ast.arguments(args=[],
                                                  defaults=[], vararg=None, kwarg=None),
                               body=[ast.Expr(decl) for decl in decls],
                               decorator_list=[])
        return [init]

    @staticmethod
    def load_stream(env, stream):
        codes = []
        for form in shen_reader(stream):
            for code in env.eval(form):
                codes.append(code)
        return codes

class Shen2(ShenEnv):
    def __init__(self):
        ShenEnv.__init__(self)
        self.set(Sym("*language*"), "Python")
        self.set(Sym("*implementation*"), "")
        self.set(Sym("*release*"), 0)
        self.set(Sym("*port*"), 0)
        self.set(Sym("*porters*"), "")
        self.set(Sym("*home-directory*"), "")
        self.set(Sym("*stinput*"), sys.stdin)
        self.set(Sym("*stoutput*"), sys.stdout)
        #load k-lambda
        k_files = os.listdir("k_lambda")
        k_files.sort()
        fpo  = open("/tmp/shen.py", "w+")
        for file in k_files:
            print "loading file", file
            fpo.write("#" + "=" * 30 + " " + file + "=" * 30 + "\n\n")
            fp = open("k_lambda/" + file, "r")
            module = ShenEnv.load_stream(self, fp)
            unparse.Unparser(module, fpo)
            fp.close()
            print self.FUNCTIONS
            break
        fpo.close()

def compile_pyshen():
    global SYMDIC, SYMDIC_MODE
    SYMDIC_MODE = True
    env = ShenEnv()
    shen_decls = [
        ast.parse('FUNCTIONS.update({"or": shen_or, "and": shen_and})'),
        ast.parse('VARS.update({"*language*": "Python", "*implementation*": "pyshen", "*release*": "", "*port*": "0.135", "*porters*": "Matthieu Lagacherie and Yannick Drant", "*home-directory*": "~/", "*stinput*": sys.stdin, "*stoutput*": sys.stdout, "*version*": "version 11"})')]
    shen_postdecls = [ast.parse("shen_initialise_arity_table(shen_to_cons([Sym('absvector'), 1, Sym('adjoin'), 2, Sym('and'), 2, Sym('append'), 2, Sym('arity'), 1, Sym('assoc'), 2, Sym('boolean?'), 1, Sym('cd'), 1, Sym('compile'), 3, Sym('concat'), 2, Sym('cons'), 2, Sym('cons?'), 1, Sym('cn'), 2, Sym('declare'), 2, Sym('destroy'), 1, Sym('difference'), 2, Sym('do'), 2, Sym('element?'), 2, Sym('empty?'), 1, Sym('enable-type-theory'), 1, Sym('interror'), 2, Sym('eval'), 1, Sym('eval-kl'), 1, Sym('explode'), 1, Sym('external'), 1, Sym('fail-if'), 2, Sym('fail'), 0, Sym('fix'), 2, Sym('findall'), 5, Sym('freeze'), 1, Sym('fst'), 1, Sym('gensym'), 1, Sym('get'), 3, Sym('get-time'), 1, Sym('address->'), 3, Sym('<-address'), 2, Sym('<-vector'), 2, Sym('>'), 2, Sym('>='), 2, Sym('='), 2, Sym('hd'), 1, Sym('hdv'), 1, Sym('hdstr'), 1, Sym('head'), 1, Sym('if'), 3, Sym('integer?'), 1, Sym('identical'), 4, Sym('inferences'), 0, Sym('intersection'), 2, Sym('length'), 1, Sym('lineread'), 0, Sym('load'), 1, Sym('<'), 2, Sym('<='), 2, Sym('vector'), 1, Sym('macroexpand'), 1, Sym('map'), 2, Sym('mapcan'), 2, Sym('maxinferences'), 1, Sym('not'), 1, Sym('nth'), 2, Sym('n->string'), 1, Sym('number?'), 1, Sym('occurs-check'), 1, Sym('occurrences'), 2, Sym('occurs-check'), 1, Sym('or'), 2, Sym('package'), 3, Sym('pos'), 2, Sym('print'), 1, Sym('profile'), 1, Sym('profile-results'), 0, Sym('pr'), 2, Sym('ps'), 1, Sym('preclude'), 1, Sym('preclude-all-but'), 1, Sym('protect'), 1, Sym('address->'), 3, Sym('put'), 4, Sym('shen.reassemble'), 2, Sym('read-file-as-string'), 1, Sym('read-file'), 1, Sym('read-byte'), 1, Sym('read-from-string'), 1, Sym('remove'), 2, Sym('reverse'), 1, Sym('set'), 2, Sym('simple-error'), 1, Sym('snd'), 1, Sym('specialise'), 1, Sym('spy'), 1, Sym('step'), 1, Sym('stinput'), 0, Sym('stoutput'), 0, Sym('string->n'), 1, Sym('string->symbol'), 1, Sym('string?'), 1, Sym('shen.strong-warning'), 1, Sym('subst'), 3, Sym('shen.sum'), 1, Sym('symbol?'), 1, Sym('tail'), 1, Sym('tl'), 1, Sym('tc'), 1, Sym('tc?'), 1, Sym('thaw'), 1, Sym('track'), 1, Sym('trap-error'), 2, Sym('tuple?'), 1, Sym('type'), 1, Sym('return'), 3, Sym('undefmacro'), 1, Sym('unprofile'), 1, Sym('unify'), 4, Sym('unify!'), 4, Sym('union'), 2, Sym('untrack'), 1, Sym('unspecialise'), 1, Sym('undefmacro'), 1, Sym('vector'), 1, Sym('vector->'), 3, Sym('value'), 1, Sym('variable?'), 1, Sym('version'), 1, Sym('warn'), 1, Sym('write-to-file'), 2, Sym('y-or-n?'), 1, Sym('+'), 2, Sym('*'), 2, Sym('/'), 2, Sym('-'), 2, Sym('=='), 2, Sym('shen.<1>'), 1, Sym('<e>'), 1, Sym('@p'), 2, Sym('@v'), 2, Sym('@s'), 2, Sym('preclude'), 1, Sym('include'), 1, Sym('preclude-all-but'), 1, Sym('include-all-but'), 1, Sym('where'), 2]))"),
                  ast.parse("kl_put(shen_intern('shen'), Sym('shen.external-symbols'), shen_to_cons([Sym('!'), Sym('}'), Sym('{'), Sym('-->'), Sym('<--'), Sym('&&'), Sym(':'), Sym(';'), Sym(':-'), Sym(':='), Sym('_'), Sym('*language*'), Sym('*implementation*'), Sym('*stinput*'), Sym('*home-directory*'), Sym('*version*'), Sym('*maximum-print-sequence-size*'), Sym('*macros*'), Sym('*os*'), Sym('*release*'), Sym('*property-vector*'), Sym('@v'), Sym('@p'), Sym('@s'), Sym('*port*'), Sym('*porters*'), Sym('<-'), Sym('->'), Sym('<e>'), Sym('=='), Sym('='), Sym('>='), Sym('>'), Sym('/.'), Sym('=!'), Sym('$'), Sym('-'), Sym('/'), Sym('*'), Sym('+'), Sym('<='), Sym('<'), Sym('>>'), tco_apply(kl_vector, [0]), Sym('==>'), Sym('y-or-n?'), Sym('write-to-file'), Sym('where'), Sym('when'), Sym('warn'), Sym('version'), Sym('verified'), Sym('variable?'), Sym('value'), Sym('vector->'), Sym('<-vector'), Sym('vector'), Sym('vector?'), Sym('unspecialise'), Sym('untrack'), Sym('unit'), Sym('shen.unix'), Sym('union'), Sym('unify'), Sym('unify!'), Sym('unprofile'), Sym('undefmacro'), Sym('return'), Sym('type'), Sym('tuple?'), Sym('true'), Sym('trap-error'), Sym('track'), Sym('time'), Sym('thaw'), Sym('tc?'), Sym('tc'), Sym('tl'), Sym('tlstr'), Sym('tlv'), Sym('tail'), Sym('systemf'), Sym('synonyms'), Sym('symbol'), Sym('symbol?'), Sym('string->symbol'), Sym('subst'), Sym('string?'), Sym('string->n'), Sym('stream'), Sym('string'), Sym('stinput'), Sym('stoutput'), Sym('step'), Sym('spy'), Sym('specialise'), Sym('snd'), Sym('simple-error'), Sym('set'), Sym('save'), Sym('str'), Sym('run'), Sym('reverse'), Sym('remove'), Sym('read'), Sym('read-file'), Sym('read-file-as-bytelist'), Sym('read-file-as-string'), Sym('read-byte'), Sym('read-from-string'), Sym('quit'), Sym('put'), Sym('preclude'), Sym('preclude-all-but'), Sym('ps'), Sym('prolog?'), Sym('protect'), Sym('profile-results'), Sym('profile'), Sym('print'), Sym('pr'), Sym('pos'), Sym('package'), Sym('output'), Sym('out'), Sym('or'), Sym('open'), Sym('occurrences'), Sym('occurs-check'), Sym('n->string'), Sym('number?'), Sym('number'), Sym('null'), Sym('nth'), Sym('not'), Sym('nl'), Sym('mode'), Sym('macro'), Sym('macroexpand'), Sym('maxinferences'), Sym('mapcan'), Sym('map'), Sym('make-string'), Sym('load'), Sym('loaded'), Sym('list'), Sym('lineread'), Sym('limit'), Sym('length'), Sym('let'), Sym('lazy'), Sym('lambda'), Sym('is'), Sym('intersection'), Sym('inferences'), Sym('intern'), Sym('integer?'), Sym('input'), Sym('input+'), Sym('include'), Sym('include-all-but'), Sym('in'), Sym('if'), Sym('identical'), Sym('head'), Sym('hd'), Sym('hdv'), Sym('hdstr'), Sym('hash'), Sym('get'), Sym('get-time'), Sym('gensym'), Sym('function'), Sym('fst'), Sym('freeze'), Sym('fix'), Sym('file'), Sym('fail'), Sym('fail-if'), Sym('fwhen'), Sym('findall'), Sym('false'), Sym('enable-type-theory'), Sym('explode'), Sym('external'), Sym('exception'), Sym('eval-kl'), Sym('eval'), Sym('error-to-string'), Sym('error'), Sym('empty?'), Sym('element?'), Sym('do'), Sym('difference'), Sym('destroy'), Sym('defun'), Sym('define'), Sym('defmacro'), Sym('defcc'), Sym('defprolog'), Sym('declare'), Sym('datatype'), Sym('cut'), Sym('cn'), Sym('cons?'), Sym('cons'), Sym('cond'), Sym('concat'), Sym('compile'), Sym('cd'), Sym('cases'), Sym('call'), Sym('close'), Sym('bind'), Sym('bound?'), Sym('boolean?'), Sym('boolean'), Sym('bar!'), Sym('assoc'), Sym('arity'), Sym('append'), Sym('and'), Sym('adjoin'), Sym('<-address'), Sym('address->'), Sym('absvector?'), Sym('absvector'), Sym('abort')]), shen_get(Sym('*property-vector*')))")]
    shen_body = shen_decls
    #load k-lambda
    for file in ["toplevel.kl", "core.kl", "sys.kl", "sequent.kl", "yacc.kl", "reader.kl", "prolog.kl", "track.kl", "load.kl", "writer.kl", "macros.kl", "declarations.kl", "types.kl", "t-star.kl"]:
        print "loading file", file
        shen_body.append(str("#" + "=" * 30 + " " + file + "=" * 30 + "\n\n"))
        fp = open("k_lambda/" + file, "r")
        codes = ShenEnv.load_stream(env, fp)
        # print codes
        # unparse.Unparser(module, fpo)
        fp.close()
        for code in codes:
            if isinstance(code, ast.Call) and code.func.id == "apply":
                shen_postdecls.append(ast.Expr(code))
                # print ast.dump(code), code.func
            elif not isinstance(code, ast.FunctionDef) :
                shen_body.append(ast.Expr(code))
            else:
                shen_body.append(code)
        # if file == "declarations.kl":
    shen_body += shen_postdecls
    # print shen_body
    module_body = [ast.parse("import sys\nfrom pyshen import *\n")]
    # module_body += env.getDeclarations(shen_decls, shen_postdecls) + shen_body
    module_body += [ast.parse("class SymDic:\n" + "\n".join(["  %s = Sym('%s')" %(SYMDIC[sym], sym) for sym in SYMDIC])
                              + "\nsymdic = SymDic()\n")]
    module_body += shen_body
    module = ast.Module(body=module_body)
    fix(module)
    fpo  = open("shen.py", "w+")
    fpo.write(open("header.py", "r").read())
    fpo.write("\n")
    unparse.Unparser(module, fpo)
    # fpo.write('\ndef pyshen(): [shen_init(), shen_eval_kl(shen_to_cons([Sym("shen.shen")]), globals())]\n')
    fpo.write(open("footer.py", "r").read())
    fpo.close()
    SYMDIC_MODE = False

from shen import *

def pyshen():
    shen_eval_kl(shen_to_cons([Sym("shen.shen")]), globals())
