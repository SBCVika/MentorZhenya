
# Functions

def func(b, c):
    print(b, c)


a = {1: 45, 2: 6}

for param in a:
    print(param)

func(c=4, b=3)
func(*a)    # TODO pay attention to such kind of call  where a is a dict !!!
print('*' * 15)

"""
function that computes avg accourding to condition:
    1: sum()/len()
    2: sum()/min()
"""

COMP_METHOD_AVG = 0
COMP_METHOD_MIN = 1

def avg(b, *args, **kwargs):
    print(b)
    print(f"{args=}")
    print(f"{kwargs=}")
    c = kwargs.get('comp_method', COMP_METHOD_AVG)
    if c == 0:
        return sum((b,) + args) / (len(args) + 1)
    elif c == 1:
        return sum((b,) + args) / min((b,) + args)
    elif c == 2:
        return sum((b,) + args) / max((b,) + args)
    else:
        raise ValueError('Error unknown algorythm')


av = None
try:
    av = avg(5, 5, 6, 7, comp_method=5)   # `av` not exists if Exception
except ValueError:
    pass
print(av)

l = [1, 2, 4, 56]
b, c, f, e = l

print(f'{e=}')

print('*' * 15)

COMP_METHOD = {
    0: lambda *args: sum(args) / (len(args)),  # sum(args) = sum((3,4,6,7,8)) -> 28
    1: lambda *args: sum(args) / (min(*args)),  # sum(*args) = sum(3,4,6,7,8) -> error
    2: lambda *args: sum(args) / (max(*args)),
}


def avg(b, *args, **kwargs):
    """
    Computes avg by condition `comp_method`
    :param b: int: first value
    :param args: tuple[int]: ither values
    :param kwargs: kwargs['comp_method']: identifies what algo shound be used
    :return: float: or raises ValueError if error
    """
    print(f"{args=}")
    print(f"{kwargs=}")
    c = kwargs.get('comp_method', COMP_METHOD_AVG)
    func = COMP_METHOD.get(c)
    if func is None:
        raise ValueError('Error unknown algorythm')
    return func(*((b,) + args))

print(help(avg))
print(f'avg={avg(3,4,6,7,8, comp_method=0)}')
print(f'avg={avg(3,4,6,7,8, comp_method=1)}')
print(f'avg={avg(3,4,6,7,8, comp_method=2)}')

g = avg
g.ret = 5
print(g.__name__)
print(g.__doc__)
print(avg.ret)

print('*' * 15)

range(100)           # 0, 1, 2, 3, ..., 99        - [0, 100)
range(10, 100)       # 10, 11, 12, 13, ..., 99    - [10, 100)
range(10, 100, 2)    # 10, 12, 14, 16, ..., 98    - [10, 98]
range(100, 10, -2)   # 100, 98, 96, 94, ..., 12   - [100, 10]


# func that computes factorial of `n` with loop
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def fact_while(n):
    res = 1
    i = 1
    while i < n + 1:
        res *= i
        i += 1
    return res


print(f'while= {fact_while(5)}')
assert fact(5) == fact_while(5), "Fact not equal to recursive one"


def fact_rec(n):
    if n > 1:
        return fact_rec(n - 1) * n
    else:
        return 1

#  fact_rec(5) => fact_rec(fact_rec(fact_rec(1 * 2) * 3) * 4) * 5


print(fact_rec(5))
assert fact(5) == fact_rec(5), "Fact not equal to recursive one"

# tasks for loops (for, while)
# tasks for functions
# hexeditor
