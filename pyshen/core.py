# core.py ---
import ast
import re

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
    SYMS = ['!', '}', '{', '-->', '<--', '&&', ':', ';', ':-', ':=', '_', '*language*', '*implementation*', '*stinput*', '*home-directory*', '*version*', '*maximum-print-sequence-size*', '*macros*', '*os*', '*release*', '*property-vector*', '@v', '@p', '@s', '*port*', '*porters*', '<-', '->', '<e>', '==', '=', '>=', '>', '/.', '=!', '$', '-', '/', '*', '+', '<=', '<', '>>', '==>', 'y-or-n?', 'write-to-file', 'where', 'when', 'warn', 'version', 'verified', 'variable?', 'value', 'vector->', '<-vector', 'vector', 'vector?', 'unspecialise', 'untrack', 'unit', 'shen.unix', 'union', 'unify', 'unify!', 'unprofile', 'undefmacro', 'return', 'type', 'tuple?', "false", 'trap-error', 'track', 'time', 'thaw', 'tc?', 'tc', 'tl', 'tlstr', 'tlv', 'tail', 'systemf', 'synonyms', 'symbol', 'symbol?', 'string->symbol', 'subst', 'string?', 'string->n', 'stream', 'string', 'stinput', 'stoutput', 'step', 'spy', 'specialise', 'snd', 'simple-error', 'set', 'save', 'str', 'run', 'reverse', 'remove', 'read', 'read-file', 'read-file-as-bytelist', 'read-file-as-string', 'read-byte', 'read-from-string', 'quit', 'put', 'preclude', 'preclude-all-but', 'ps', 'prolog?', 'protect', 'profile-results', 'profile', 'print', 'pr', 'pos', 'package', 'output', 'out', 'or', 'open', 'occurrences', 'occurs-check', 'n->string', 'number?', 'number', 'null', 'nth', 'not', 'nl', 'mode', 'macro', 'macroexpand', 'maxinferences', 'mapcan', 'map', 'make-string', 'load', 'loaded', 'list', 'lineread', 'limit', 'length', 'let', 'lazy', 'lambda', 'is', 'intersection', 'inferences', 'intern', 'integer?', 'input', 'input+', 'include', 'include-all-but', 'in', 'if', 'identical', 'head', 'hd', 'hdv', 'hdstr', 'hash', 'get', 'get-time', 'gensym', 'function', 'fst', 'freeze', 'fix', 'file', 'fail', 'fail-if', 'fwhen', 'findall', "true", 'enable-type-theory', 'explode', 'external', 'exception', 'eval-kl', 'eval', 'error-to-string', 'error', 'empty?', 'element?', 'do', 'difference', 'destroy', 'defun', 'define', 'defmacro', 'defcc', 'defprolog', 'declare', 'datatype', 'cut', 'cn', 'cons?', 'cons', 'cond', 'concat', 'compile', 'cd', 'cases', 'call', 'close', 'bind', 'bound?', 'boolean?', 'boolean', 'bar!', 'assoc', 'arity', 'append', 'and', 'adjoin', '<-address', 'address->', 'absvector?', 'absvector', 'abort', "super", "exists", "assert", "for", "while"]
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
        if self.sym in self.SYMS:
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

class SException(Exception):
    pass

