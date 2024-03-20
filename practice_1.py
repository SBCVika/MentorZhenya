
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
