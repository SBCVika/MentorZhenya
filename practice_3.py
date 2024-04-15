import re
from datetime import datetime, timedelta
from time import perf_counter


# Extended functions - generators, decorators

def measure_time(func):

    def wrapper(*args, **kwargs):
        t1_start = perf_counter()
        result = func(*args, **kwargs)
        t1_stop = perf_counter()
        print("Elapsed time:", func.__name__, f'{t1_stop - t1_start:0.6f}')
        return result

    return wrapper


def compare_versions(ver1, ver2):
    regex = re.compile(r'\d+')
    ver1_num = [int(m.group(0)) for m in re.finditer(regex, ver1)]
    ver2_num = [int(m.group(0)) for m in re.finditer(regex, ver2)]
    lv1, lv2 = len(ver1_num), len(ver2_num)
    for i in range(min(len(ver1_num), len(ver2_num))):
        if ver1_num[i] > ver2_num[i]:
            return 1
        elif ver1_num[i] < ver2_num[i]:
            return -1

    if len(ver1_num) > len(ver2_num):
        return 1
    elif len(ver1_num) < len(ver2_num):
        return -1
    else:
        return 0


@measure_time
def print_version():
    pass
# @measure_time
# def compare_versions(ver1, ver2):
# OR

origin_function = compare_versions
def refunc():
    compare_version_func = measure_time(compare_versions)
    print(compare_version_func('1.2', '1.3'))
    print(compare_version_func('1.4', '1.3'))

refunc()
print(compare_versions('1.23', '1.3'))


# Generator

print(list(range(10)))
def range_gen(n):
    start = 0
    while start < n:
        yield start
        start += 1


for item in range_gen(10):
    print(item)


def gen_date_from_now():
    now = datetime.now()
    while True:
        yield now.date()
        now = now + timedelta(days=1)


gen = gen_date_from_now()

for i in range(100):
    print(next(gen))

for i in range(10):
    print(next(gen))


def gen_even(start_number):
    while True:
        yield start_number
        start_number += 2


def filter_zeros(gen):
    while True:
        number = next(gen)
        if number % 10 == 0:
            yield number
            break


g = gen_even(4564)
filtered = filter_zeros(g)
for f in filtered:
    print(f)

# tail -f

# читати файл і виводити лише те що добавилось (зробити а допомогою генератора):
#    створити 2 прогшрами , одна пише у файл з проміжком 1 сек - кожну секунду дописує стрічку у визн файл
#    друга - при запуску вичитує весь файл на екран і чекає наступних рядків

import practice_4