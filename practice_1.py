
# Lists are the same (and why)
g = ["gtr", "gtr", "grwe", None, "fgre"]
b = g
b[0] = 100

l = [100, "gtr", "grwe", None, "fgre"]

# Comparing objects
print(b is g)
print(b == g)
print(b is l)
print(b == l)



# Data types
int(5.5)
int("5")
print(2**100)
print(int("0733", base=8))

print(bin(-1 & 0xFF))

print(int(False))
print(bool(None))

s = set('oaieu')
print(sum(i in s for i in "mfreogpamfrekgroa"))
print(f'{54300000:,}')

# TODO setup venv and IDE (pycharm)
# TODO how to print values and debug
# f-string format int float
# TODO int, bool, float
# file (text, binary)


# Task 1
"""
  1. print out numbers
     for given list of numbers: e.g [13,4,4,5,32,2,6,54,32]
        1.1 print number only if it less then previus one: for example above: [4, 2, 32] 
        1.2 print out hex representation of numbers (numbers will be only within 1 byte 0..255) 
            without 0x: for numbers above: 0D 04 04 05 20 02 06 36 20
     
     for given list of numbers: e.g [1.2, 0.34, 1.4, 2.5434]
        1.3 print 2 sums of numbers: 1) less then 1 (0.34)   2) more or eq to 1 (5.1434) 
        1.4 print number for such `n`, with given threshold `t`
            e.g.  n=1.3 t=0.2  -  [1.2, 1.4]
                  n=1.0 t=1.0  -  [1.2, 0.34, 1.4]
                  n=1.0 t=0.1  -  []
"""