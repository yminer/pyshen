# stream.pyx ---
import sys
from libc.stdio cimport fopen, fclose, FILE, fread, fwrite
cimport libc.stdio
from pyshen.core import PartialDecorator, Sym, SException

cdef class File:
    cdef FILE *fp

    def __init__(self):
        pass

    def open(self, name, flags):
        self.fp = fopen(name, flags)

    def close(self):
        fclose(self.fp)

    def read(self):
        cdef char tok
        if fread(&tok, 1, 1, self.fp) == 1:
            return tok
        else:
            return -1

    def write(self, char *s, int len):
        fwrite(s, 1, len, self.fp)

def shen_stdin():
    f = File()
    f.fp = libc.stdio.stdin
    return f

def shen_stdout():
    f = File()
    f.fp = libc.stdio.stdout
    return f

def shen_open(stream_type, name, direction):
    if not stream_type.sym == "file":
        raise SException("unsupported stream type")
    f = File()
    f.open(name, "w" if direction.sym == "out" else "r")
    return f

def shen_close(File stream):
    stream.close()

def shen_pr(char *s, File stream):
    stream.write(s, len(s))
    return s

def shen_read_byte(File stream):
    return stream.read()

