

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # print("Name", cls.__name__)
        inst = cls._instances.get(cls.__name__, None)
        if inst is None:
            inst = super().__call__(*args, **kwargs)
            cls._instances[cls.__name__] = inst
        # print("Instances", cls._instances)
        return inst


class Template(metaclass=Singleton):
    def __init__(self, a):
        self.a = a

    def get_a(self):
        return self.a


class Template1(Template):
    pass


# print(Template(4))
# print(Template(5) is Template(6)) # None is None
# print(Template(7) is Template(8))
# print(Template1(10))
# print("A", Template(100).get_a())


import json

# create Config (should read configs from file.json) and ap[ply to object Field
# use custom iterator that will be used as a generator of circles

class Config(metaclass=Singleton):
    def __init__(self):
        self.d = json.load(open('file.json'))

config = Config()

# print(d)


class CycleIter:
    def __init__(self, iterable):
        self._iter = list(iterable)
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = self._iter[self._idx % len(self._iter)]
        self._idx += 1
        return res


l = [1,2,4,5]
iterable = CycleIter(l)

for idx in range(100):
        print(idx, next(iterable))