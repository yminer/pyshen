# stream.py ---
import sys

def shen_stdin():
    return sys.stdin

def shen_stdout():
    return sys.stdout

def shen_open(stream_type, name, direction):
    # print "Opening", stream_type, name, direction, type(direction)
    if not stream_type.sym == "file":
        raise SException("unsupported stream type")
    try:
        return open(name, "w" if direction.sym == "out" else "r")
    except IOError, e:
        raise SException("IOError: " + e.message)

def shen_close(stream):
    stream.close()

def shen_pr(s, stream):
    if stream == sys.stdin:
        stream = sys.stdout
    stream.write(s)
    return s

def shen_read_byte(stream):
    rd = stream.read(1)
    return ord(rd) if len(rd) > 0 else -1

