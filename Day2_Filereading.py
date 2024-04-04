import re
from time import perf_counter
#1 . написати функцію яка відкриває текстовий файл і повертає дані )
#2. написати функцію яка вимірює час виконання функції з пункту (1.) вивести час та імя функції
#    використати time.perf_counter() для заміру часу
#напиши функцію яка порівнює версії програм
#напр 1.1 > 1.0.9
#1.0.1 == 1.0.1
#1.0 < 1.0.1
#функція має так сигнатуру def compare_versions(ver1, ver2):
#подумай над тим що має бути результатом

def compare_versions(ver1, ver2):
    regex = re.compile(r'\d+')
    ver1_num = [int(num) for num in re.findall(regex, ver1)]
    ver2_num = [int(num) for num in re.findall(regex, ver2)]

    for i in range(min(len(ver1_num), len(ver2_num))):
        if ver1_num[i] > ver2_num[i]:
            return "new"
        elif ver1_num[i] < ver2_num[i]:
            return "old"

    if len(ver1_num) > len(ver2_num):
        return "new"
    elif len(ver1_num) < len(ver2_num):
        return "old"
    elif len(ver1_num) == len(ver2_num):
        return "same"
def Readfile(filename):

    file = open('versions.txt', 'r')
    versions = file.readlines()  # I use readline instead of read because I would like to use output like a list
    file.close()
    return versions
t1_start = perf_counter()
versions = Readfile('versions.txt')
t1_stop = perf_counter()
print("Elapsed time:", t1_stop, t1_start)
print(versions)
ver1 = versions[-1]
ver2 = versions[-2]

if compare_versions(ver1, ver2) == "new":
    print(f"Released new version {ver1}")
elif compare_versions(ver1, ver2) == "old":
    print("There are no new versions")
elif compare_versions(ver1, ver2) == "same":
    print("Same version is released")
