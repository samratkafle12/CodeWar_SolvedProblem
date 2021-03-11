import math
from math import sqrt
def is_square(n):  
    if n < 0:
        return False
    
    elif (int (math.isqrt(n) ** 2 == n)):
        return True
    else:
        return False

n = 4

print(is_square(n))