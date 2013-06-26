#  -*- Mode: Python -*- 
import os
import sys
import re
import numbers
import ast
import StringIO
import copy
import itertools
import unparse
import contextlib
import time
import uuid
import functools
import inspect

################################################################################
################################   ENVIRONMENT   ###############################
################################################################################

sys.setrecursionlimit(10000)
FUNCTIONS = dict()
FUNARITIES = dict()
VARS = dict()

from pyshen.core import *

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


from pyshen.primitives import *

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
    global FUNCTIONS
    FUNCTIONS[intern(name)] = fun
    return Sym(name)

def shen_get_fun(name):
    global FUNCTIONS
    try:
        return FUNCTIONS[name]
    except Exception, e:
        raise SException(e.message)

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
        try:
            result = apply(fun, args)
        except TypeError, e:
            try:
                arity = fun.arity
            except AttributeError, e1:
                arity = len(inspect.getargspec(fun).args)
                fun.arity = arity
            argsize = len(args)
            if arity > argsize:
                result = functools.partial(fun, *args)
                result.arity = arity - argsize
            else:
                #uncurrying, from Shen-Ruby implementation
                fun = tco_apply(fun, args[0:arity])
                if not (isinstance(fun, Sym) or hasattr(fun, "__call__")):
                    raise SException("the value " + str(fun) + " is not a Sym or a function")
                args = args[arity:]
                continue
        if tramp_fn:
            args = tramp_args
            tramp_args = None
            fun = tramp_fn
        else:
            fun = None
    return result

def tail_recursion(func):
    return func

def kl_quit():
    sys.exit(1)

################################################################################
################################   PARSER   ####################################
################################################################################
def shen_compile(form, rvalue=False):
    env = ShenEnv()
    code = env.compile_shen(form)
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
    # ShenVisitorPartial().visit(module)
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
        exec(bcode) in glob#, ldict)
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
    currentfun = None
    count = 0
    
    def gensym(self):
        self.count += 1
        return "%s_lambda_%d" %(self.currentfun, self.count)
    def visit_Call(self, node):
        # if node.func.id=="apply" and isinstance(node.args[0], ast.Lambda):
        #     self.generic_visit(node)
        #     if not isinstance(node.args[0], ast.FunctionDef):
        #         raise SException("ast transforamtion failed " + node.args)
        #     fun = node.args[0]
        #     node.args[0] = ast.Name(id=fun.name, ctx=ast.Load(), lineno=1, col_offset=0)
        #     node.lineno = node.col_offset = 1
        #     fix(node)
        #     return node
        # self.generic_visit(node)
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
    #     body[-1] = ast.Return(body[-1], lineno=1, col_offset=0)
    #     node = ast.FunctionDef(name=self.gensym(),
    #                            args=node.args,
    #                            body=body, decorator_list=[], lineno=1, col_offset=0)
    #     node.lineno = node.col_offset = 1
    #     fix(node)
    #     self.localfuns = saved
    #     self.localfuns.append(node)
    #     return ast.Name(id=node.name, ctx=ast.Load(), lineno=1, col_offset=0)
    def visit_FunctionDef(self, node):
        savedloc = self.localfuns
        savedfun = self.currentfun
        self.localfuns = []
        self.currentfun = node.name
        self.generic_visit(node)
        nbody = []
        nloc = min(2, node.nlocals)
        for fun in self.localfuns:
            fix(fun)
            nbody.append(fun)
        # print "LOCFUN", self.localfuns
        for line in range(len(node.body)):
            if line < nloc:
                nbody.insert(line, node.body[line])
            else:
                nbody.append(node.body[line])
        # nbody += node.body
        nbody[-1] = ast.Return(nbody[-1], lineno=1)
        node.body = nbody
        fix(node)
        self.localfuns = savedloc
        self.currentfun = savedfun
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
        '=': (2, lambda x, y: ast.Compare(left=x, ops=[ast.Eq()], comparators=[y]),# ast.Call(func=ast.Name(id='shen_eq', ctx=ast.Load()), keywords=[], starargs=None, kwargs=None, args=[x, y]),
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
        try:
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
        except Exception, e:
            print "compilation failed", e
            raise e

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
                # ShenVisitorPartial().visit(c)
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
    symdic_set_status(True)
    env = ShenEnv()
    shen_decls = [
        ast.parse('FUNCTIONS.update({"or": shen_or, "and": shen_and})'),
        ast.parse('VARS.update({"*language*": "Python", "*implementation*": "pyshen", "*release*": "", "*port*": "0.136", "*porters*": "Matthieu Lagacherie and Yannick Drant", "*home-directory*": "~/", "*stinput*": shen_stdin(), "*stoutput*": shen_stdout(), "*version*": "version 12"})')]
    shen_postdecls = [
        ast.parse("shen_initialise_arity_table(shen_to_cons([Sym('absvector'), 1, symdic.symdic_kl_adjoin, 2, symdic.symdic_kl_and, 2, symdic.symdic_kl_append, 2, symdic.symdic_kl_arity, 1, symdic.symdic_kl_assoc, 2, symdic.symdic_kl_booleanx63, 1, symdic.symdic_kl_cd, 1, symdic.symdic_kl_compile, 3, Sym('concat'), 2, symdic.symdic_kl_cons, 2, symdic.symdic_kl_consx63, 1, symdic.symdic_kl_cn, 2, Sym('declare'), 2, symdic.symdic_kl_destroy, 1, symdic.symdic_kl_difference, 2, symdic.symdic_kl_do, 2, symdic.symdic_kl_elementx63, 2, symdic.symdic_kl_emptyx63, 1, symdic.symdic_kl_enablex45typex45theory, 1, Sym('interror'), 2, Sym('eval'), 1, symdic.symdic_kl_evalx45kl, 1, symdic.symdic_kl_explode, 1, symdic.symdic_kl_external, 1, symdic.symdic_kl_failx45if, 2, symdic.symdic_kl_fail, 0, symdic.symdic_kl_fix, 2, symdic.symdic_kl_findall, 5, symdic.symdic_kl_freeze, 1, symdic.symdic_kl_fst, 1, symdic.symdic_kl_gensym, 1, symdic.symdic_kl_get, 3, symdic.symdic_kl_getx45time, 1, symdic.symdic_kl_addressx45x62, 3, symdic.symdic_kl_x60x45address, 2, symdic.symdic_kl_x60x45vector, 2, symdic.symdic_kl_x62, 2, symdic.symdic_kl_x62x61, 2, symdic.symdic_kl_x61, 2, symdic.symdic_kl_hd, 1, symdic.symdic_kl_hdv, 1, symdic.symdic_kl_hdstr, 1, symdic.symdic_kl_head, 1, symdic.symdic_kl_if, 3, symdic.symdic_kl_integerx63, 1, symdic.symdic_kl_intern, 1, symdic.symdic_kl_identical, 4, symdic.symdic_kl_inferences, 0, symdic.symdic_kl_intersection, 2, symdic.symdic_kill, 0, symdic.symdic_kl_length, 1, symdic.symdic_kl_lineread, 0, symdic.symdic_kl_load, 1, symdic.symdic_kl_x60, 2, symdic.symdic_kl_x60x61, 2, symdic.symdic_kl_vector, 1, symdic.symdic_kl_macroexpand, 1, symdic.symdic_kl_map, 2, symdic.symdic_kl_mapcan, 2, symdic.symdic_kl_maxinferences, 1, symdic.symdic_kl_not, 1, symdic.symdic_kl_nth, 2, symdic.symdic_kl_nx45x62string, 1, symdic.symdic_kl_numberx63, 1, symdic.symdic_kl_occursx45check, 1, symdic.symdic_kl_occurrences, 2, symdic.symdic_kl_occursx45check, 1, symdic.symdic_optimise, 1, symdic.symdic_kl_or, 2, symdic.symdic_kl_package, 3, symdic.symdic_kl_pos, 2, symdic.symdic_kl_print, 1, symdic.symdic_kl_profile, 1, symdic.symdic_kl_profilex45results, 0, symdic.symdic_kl_pr, 2, symdic.symdic_kl_ps, 1, symdic.symdic_kl_preclude, 1, symdic.symdic_kl_precludex45allx45but, 1, symdic.symdic_kl_protect, 1, symdic.symdic_kl_addressx45x62, 3, symdic.symdic_kl_put, 4, Sym('shen.reassemble'), 2, symdic.symdic_kl_readx45filex45asx45string, 1, symdic.symdic_kl_readx45file, 1, symdic.symdic_kl_readx45byte, 1, symdic.symdic_kl_readx45fromx45string, 1, symdic.symdic_kl_remove, 2, symdic.symdic_kl_reverse, 1, symdic.symdic_kl_set, 2, symdic.symdic_kl_simplex45error, 1, symdic.symdic_kl_snd, 1, symdic.symdic_kl_specialise, 1, symdic.symdic_kl_spy, 1, symdic.symdic_kl_step, 1, symdic.symdic_kl_stinput, 0, symdic.symdic_kl_stoutput, 0, symdic.symdic_kl_stringx45x62n, 1, symdic.symdic_kl_stringx45x62symbol, 1, symdic.symdic_kl_stringx63, 1, Sym('shen.strong-warning'), 1, symdic.symdic_kl_subst, 3, symdic.symdic_shen_sum, 1, symdic.symdic_kl_symbolx63, 1, symdic.symdic_kl_tail, 1, symdic.symdic_kl_tl, 1, symdic.symdic_kl_tc, 1, symdic.symdic_kl_tcx63, 1, symdic.symdic_kl_thaw, 1, symdic.symdic_kl_tlstr, 1, symdic.symdic_kl_track, 1, symdic.symdic_kl_trapx45error, 2, symdic.symdic_kl_tuplex63, 1, symdic.symdic_kl_type, 1, symdic.symdic_kl_return, 3, symdic.symdic_kl_undefmacro, 1, symdic.symdic_kl_unprofile, 1, symdic.symdic_kl_unify, 4, symdic.symdic_kl_unifyx33, 4, symdic.symdic_kl_union, 2, symdic.symdic_kl_untrack, 1, symdic.symdic_kl_unspecialise, 1, symdic.symdic_kl_undefmacro, 1, symdic.symdic_kl_vector, 1, symdic.symdic_kl_vectorx45x62, 3, symdic.symdic_kl_value, 1, symdic.symdic_kl_variablex63, 1, symdic.symdic_kl_version, 1, Sym('warn'), 1, symdic.symdic_kl_writex45tox45file, 2, symdic.symdic_kl_yx45orx45nx63, 1, symdic.symdic_kl_x43, 2, symdic.symdic_kl_x42, 2, symdic.symdic_kl_x47, 2, symdic.symdic_kl_x45, 2, symdic.symdic_kl_x61x61, 2, symdic.symdic_kl_x60ex62, 1, symdic.symdic_kl_x64p, 2, symdic.symdic_kl_x64v, 2, symdic.symdic_kl_x64s, 2, symdic.symdic_kl_preclude, 1, symdic.symdic_kl_include, 1, symdic.symdic_kl_precludex45allx45but, 1, symdic.symdic_kl_includex45allx45but, 1, symdic.symdic_kl_where, 2]))"),
        ast.parse("kl_put(shen_intern('shen'), symdic.symdic_shen_externalx45symbols, shen_to_cons([symdic.symdic_kl_x33, symdic.symdic_kl_x125, symdic.symdic_kl_x123, symdic.symdic_kl_x45x45x62, symdic.symdic_kl_x60x45x45, symdic.symdic_kl_x38x38, symdic.symdic_kl_x58, symdic.symdic_kl_x59, symdic.symdic_kl_x58x45, symdic.symdic_kl_x58x61, symdic.symdic_kl__, symdic.symdic_kl_x42languagex42, symdic.symdic_kl_x42implementationx42, symdic.symdic_kl_x42stinputx42, symdic.symdic_kl_x42homex45directoryx42, symdic.symdic_kl_x42versionx42, symdic.symdic_kl_x42maximumx45printx45sequencex45sizex42, symdic.symdic_kl_x42macrosx42, Sym('*os*'), Sym('*release*'), symdic.symdic_kl_x42propertyx45vectorx42, symdic.symdic_kl_x64v, symdic.symdic_kl_x64p, symdic.symdic_kl_x64s, symdic.symdic_kl_x42portx42, symdic.symdic_kl_x42portersx42, symdic.symdic_x42hushx42, symdic.symdic_kl_x60x45, symdic.symdic_kl_x45x62, symdic.symdic_kl_x60ex62, symdic.symdic_kl_x61x61, symdic.symdic_kl_x61, symdic.symdic_kl_x62x61, symdic.symdic_kl_x62, symdic.symdic_kl_x47_, symdic.symdic_kl_x61x33, symdic.symdic_kl_x36, symdic.symdic_kl_x45, symdic.symdic_kl_x47, symdic.symdic_kl_x42, symdic.symdic_kl_x43, symdic.symdic_kl_x60x61, symdic.symdic_kl_x60, symdic.symdic_kl_x62x62, tco_apply(kl_vector, [0]), symdic.symdic_kl_x61x61x62, symdic.symdic_kl_yx45orx45nx63, symdic.symdic_kl_writex45tox45file, symdic.symdic_kl_where, symdic.symdic_kl_when, Sym('warn'), symdic.symdic_kl_version, symdic.symdic_kl_verified, symdic.symdic_kl_variablex63, symdic.symdic_kl_value, symdic.symdic_kl_vectorx45x62, symdic.symdic_kl_x60x45vector, symdic.symdic_kl_vector, symdic.symdic_kl_vectorx63, symdic.symdic_kl_unspecialise, symdic.symdic_kl_untrack, symdic.symdic_kl_unit, Sym('shen.unix'), symdic.symdic_kl_union, symdic.symdic_kl_unify, symdic.symdic_kl_unifyx33, symdic.symdic_kl_unprofile, symdic.symdic_kl_undefmacro, symdic.symdic_kl_return, symdic.symdic_kl_type, symdic.symdic_kl_tuplex63, True, symdic.symdic_kl_trapx45error, symdic.symdic_kl_track, symdic.symdic_kl_time, symdic.symdic_kl_thaw, symdic.symdic_kl_tcx63, symdic.symdic_kl_tc, symdic.symdic_kl_tl, symdic.symdic_kl_tlstr, symdic.symdic_kl_tlv, symdic.symdic_kl_tail, symdic.symdic_kl_systemf, symdic.symdic_kl_synonyms, symdic.symdic_kl_symbol, symdic.symdic_kl_symbolx63, symdic.symdic_kl_stringx45x62symbol, symdic.symdic_kl_subst, symdic.symdic_kl_stringx63, symdic.symdic_kl_stringx45x62n, symdic.symdic_kl_stream, symdic.symdic_kl_string, symdic.symdic_kl_stinput, symdic.symdic_kl_stoutput, symdic.symdic_kl_step, symdic.symdic_kl_spy, symdic.symdic_kl_specialise, symdic.symdic_kl_snd, symdic.symdic_kl_simplex45error, symdic.symdic_kl_set, Sym('save'), symdic.symdic_kl_str, symdic.symdic_kl_run, symdic.symdic_kl_reverse, symdic.symdic_kl_remove, symdic.symdic_kl_read, symdic.symdic_readx43, symdic.symdic_kl_readx45file, symdic.symdic_kl_readx45filex45asx45bytelist, symdic.symdic_kl_readx45filex45asx45string, symdic.symdic_kl_readx45byte, symdic.symdic_kl_readx45fromx45string, Sym('quit'), symdic.symdic_kl_put, symdic.symdic_kl_preclude, symdic.symdic_kl_precludex45allx45but, symdic.symdic_kl_ps, symdic.symdic_kl_prologx63, symdic.symdic_kl_protect, symdic.symdic_kl_profilex45results, symdic.symdic_kl_profile, symdic.symdic_kl_print, symdic.symdic_kl_pr, symdic.symdic_kl_pos, symdic.symdic_kl_package, symdic.symdic_kl_output, symdic.symdic_kl_out, symdic.symdic_kl_or, symdic.symdic_kl_open, symdic.symdic_kl_occurrences, symdic.symdic_kl_occursx45check, symdic.symdic_kl_nx45x62string, symdic.symdic_kl_numberx63, symdic.symdic_kl_number, symdic.symdic_kl_null, symdic.symdic_kl_nth, symdic.symdic_kl_not, symdic.symdic_kl_nl, symdic.symdic_kl_mode, Sym('macro'), symdic.symdic_kl_macroexpand, symdic.symdic_kl_maxinferences, symdic.symdic_kl_mapcan, symdic.symdic_kl_map, symdic.symdic_kl_makex45string, symdic.symdic_kl_load, symdic.symdic_kl_loaded, symdic.symdic_kl_list, symdic.symdic_kl_lineread, symdic.symdic_kl_limit, symdic.symdic_kl_length, symdic.symdic_kl_let, symdic.symdic_kl_lazy, symdic.symdic_kl_lambda, symdic.symdic_kill, symdic.symdic_kl_is, symdic.symdic_kl_intersection, symdic.symdic_kl_inferences, symdic.symdic_kl_intern, symdic.symdic_kl_integerx63, symdic.symdic_kl_input, symdic.symdic_kl_inputx43, symdic.symdic_kl_include, symdic.symdic_kl_includex45allx45but, symdic.symdic_kl_in, symdic.symdic_kl_if, symdic.symdic_kl_identical, symdic.symdic_kl_head, symdic.symdic_kl_hd, symdic.symdic_kl_hdv, symdic.symdic_kl_hdstr, symdic.symdic_kl_hash, symdic.symdic_kl_get, symdic.symdic_kl_getx45time, symdic.symdic_kl_gensym, symdic.symdic_kl_function, symdic.symdic_kl_fst, symdic.symdic_kl_freeze, symdic.symdic_kl_fix, symdic.symdic_kl_file, symdic.symdic_kl_fail, symdic.symdic_kl_failx45if, symdic.symdic_kl_fwhen, symdic.symdic_kl_findall, False, symdic.symdic_kl_enablex45typex45theory, symdic.symdic_kl_explode, symdic.symdic_kl_external, symdic.symdic_kl_exception, symdic.symdic_kl_evalx45kl, Sym('eval'), symdic.symdic_kl_errorx45tox45string, symdic.symdic_kl_error, symdic.symdic_kl_emptyx63, symdic.symdic_kl_elementx63, symdic.symdic_kl_do, symdic.symdic_kl_difference, symdic.symdic_kl_destroy, symdic.symdic_kl_defun, symdic.symdic_kl_define, symdic.symdic_kl_defmacro, symdic.symdic_kl_defcc, symdic.symdic_kl_defprolog, Sym('declare'), symdic.symdic_kl_datatype, symdic.symdic_kl_cut, symdic.symdic_kl_cn, symdic.symdic_kl_consx63, symdic.symdic_kl_cons, symdic.symdic_kl_cond, Sym('concat'), symdic.symdic_kl_compile, symdic.symdic_kl_cd, symdic.symdic_kl_cases, symdic.symdic_kl_call, symdic.symdic_kl_close, symdic.symdic_kl_bind, symdic.symdic_kl_boundx63, symdic.symdic_kl_booleanx63, symdic.symdic_kl_boolean, symdic.symdic_kl_barx33, symdic.symdic_kl_assoc, symdic.symdic_kl_arity, symdic.symdic_kl_append, symdic.symdic_kl_and, symdic.symdic_kl_adjoin, symdic.symdic_kl_x60x45address, symdic.symdic_kl_addressx45x62, symdic.symdic_kl_absvectorx63, Sym('absvector'), symdic.symdic_kl_abort]), shen_get(symdic.symdic_kl_x42propertyx45vectorx42))")]
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
    fpo  = open("pyshen/shen.py", "w+")
    fpo.write(open("pyshen/header.py", "r").read())
    fpo.write("\n")
    unparse.Unparser(module, fpo)
    # fpo.write('\ndef pyshen(): [shen_init(), shen_eval_kl(shen_to_cons([Sym("shen.shen")]), globals())]\n')
    fpo.write(open("pyshen/footer.py", "r").read())
    fpo.close()
    symdic_set_status(False)

from pyshen.shen import *

def pyshen():
    shen_eval_kl(shen_to_cons([Sym("shen.shen")]), globals())

def eval_string(s):
    forms = tco_apply(Sym("read-from-string"), [s])
    result = None
    for form in shen_cons_iter(forms):
        result = tco_apply(Sym("eval"), [form])
    return result
