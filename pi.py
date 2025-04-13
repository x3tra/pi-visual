import numpy as np
import math
from decimal import Decimal as dec, getcontext

getcontext().prec = 100000

def side_size(R, n): # gets the side size of a regular polygon
    return 2 * R * math.sin(math.pi / n)

def Area(R, n): # gets the area of a regular polygon
    return (n / 2) * (R ** 2) * math.sin(2 * math.pi / n)

R = 200
n = 3

while True:
    side = side_size(R, n)
    pi = dec(Area(R, n) / (R ** 2))

    if n % 100 == 0:
        print(pi)

    n += 1
