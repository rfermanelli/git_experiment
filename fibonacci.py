import math

def fattoriale(n):
    try:
        assert (n >= 0) and (n - math.trunc(n) == 0)
        if n == 0 or n == 1:
            return 1
        else:
            return n * fattoriale(n - 1)
    except AssertionError:
        return -1
