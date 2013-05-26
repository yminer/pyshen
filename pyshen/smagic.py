#  -*- Mode: Python -*- 

import numpy as np
import pyshen

from IPython.core.magic import (Magics, magics_class, cell_magic, line_magic,
                                line_cell_magic, needs_local_scope)

@magics_class
class SMagics(Magics):
    def __init__(self, shell):
        super(SMagics, self).__init__(shell)

    @line_cell_magic
    def S(self, line, cell=None, local_ns=None):
        if cell is None:
            code = ''
            return_output = True
            line_mode = True
        else:
            code = cell
            return_output = False
            line_mode = False
        code = line + code
        result = pyshen.eval_string(code)
        if result:
            pyshen.kl_print(result)
        return result

def load_ipython_extension(ip):
    ip.register_magics(SMagics)
    
