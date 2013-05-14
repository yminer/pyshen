# PyShen

PyShen is a port of the [Shen](http://shenlanguage.org/) language to Python. This port support Shen version 11, released in May 2013.

Shen is a functional lisp with pattern matching, optional lazy evaluation, optional static type checking and an integrated prolog compiler.

This release is a [POC](http://en.wikipedia.org/wiki/Proof_of_concept) of integration of a pure functional language in the Python language. The implementation is small (~ 1300 lines of Python, 6500 lines of generated python code) and passes all the Shen Test Suite but is not yet a lightning-fast Shen implementation (in our tests, 5/6 time slower than CLisp implementation).

## Implementation

The implementation of the parser and compiler follows [ShenRuby](https://github.com/gregspurrier/shen-ruby) port of Greg Spurrier. The compiler generates directly Python bytecode with the ast module.

### Compilation of K-Lambda to Python

           +------------------+               +------------------+
           |   LEXER/PARSER   |               |     COMPILER     |
           |------------------|               |------------------|
           |Translated in CONS|               |                  |
K-Lambda-->|expressions using |+---lists----> | Generates Python |
           |Python lists      |               |     AST tree     |
           |                  |               |                  |
           +------------------+               +------------------+
                                                       +
                                                       |
                                                      AST
                                                       |                   +----------------+
                                                       v                   |    BYTECODE    |
                                              +------------------+   +----+|  (real time)   |
                                              |   AST VISITORS   |   |     +----------------+
                                              |------------------|   |
                                              |                  |   |
                                              | Transformations  |+--+
                                              | with Python AST  |   |
                                              |     visitors     |   |     +----------------+
                                              +------------------+   |     | PYTHON SOURCE  |
                                                                     +----+| (K-lambda shen |
                                                                           |  bootstrap)    |
                                                                           +----------------+

## Installation

PyShen requires Python > 2.5 and numpy. pyshen was developed and tested with Python 2.7.

## REPL

    % ipython
    In [1]: import pyshen
    In [2]: pyshen.pyshen()
    
    Shen 2010, copyright (C) 2010 Mark Tarver
    released under the Shen license
    www.shenlanguage.org, 11
    running under Python, implementation: pyshen - cpython
    port 0.135 ported by Matthieu Lagacherie and Yannick Drant


    (0-)

## Calling Python functions

Calling python functions from Shen is supported but experimental.
  
    % ipython
    In [8]: import pyshen

    In [9]: def print_hello_world(): print "hello world!"

    In [10]: pyshen.print_hello_world = print_hello_world

    In [11]: pyshen.pyshen()

    Shen 2010, copyright (C) 2010 Mark Tarver
    released under the Shen license
    www.shenlanguage.org, version 11
    running under Python, implementation: pyshen
    port 0.135 ported by Matthieu Lagacherie and Yannick Drant


    (0-) (print_hello_world)
    hello world!
    None

    (1-)