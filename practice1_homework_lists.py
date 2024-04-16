#1. print out numbers for given list of numbers: e.g [13,4,4,5,32,2,6,54,32]

int_list = [13, 4, 4, 5, 32, 2, 6, 54, 32]

# 1.1 print number only if it less then previus one: for example above: [4, 2, 32]
print("Task 1.1. Option 1 with cycle \n")
out_int = []
for i in range(1, len(int_list)):
    if int_list[i-1] > int_list[i]:
        out_int.append(int_list[i])
print(f"{out_int} \n")

print("Task 1.1 OPTION 2 - with list comprehension")

out_int = [int_list[i] for i in range(0, len(int_list)) if int_list[i] < int_list[i-1]]

print(f"{out_int} \n")
#for given list of numbers#      1.2 print out hex representation of numbers (numbers will be only within 1 byte 0..255)
#          without 0x: for numbers above: 0D 04 04 05 20 02 06 36 20''': e.g [1.2, 0.34, 1.4, 2.5434]

print("Task 1.2. HEX format")

for number in int_list:
    print('{:02x}'.format(number), end=' ')
print("\n")
#   for given list of numbers: e.g [1.2, 0.34, 1.4, 2.5434]

float_list = [1.2, 0.34, 1.4, 2.5434]

#1.3 print 2 sums of numbers: 1) less then 1 (0.34)   2) more or eq to 1 (5.1434)

print("Task 1.3. 1) Sum for numbers < 1 ")
out_float = sum(float_list[i] for i in range(len(float_list)) if float_list[i] < 1)

print(f"{out_float} \n")

print("Task 1.3. 2) Sum for numbers >= 1 ")

out_float = sum(float_list[i] for i in range(0, len(float_list)) if float_list[i] >= 1)

print(f"{out_float} \n")

#1.4 print number for such `n`, with given threshold `t`
#e.g.  n=1.3 t=0.2  -  [1.2, 1.4]
#n=1.0 t=1.0  -  [1.2, 0.34, 1.4]
#n=1.0 t=0.1  -  []"
n=1.0
t=1.0
print("Task 1.4. threshold ")

out_float = [item for item in float_list if n - t < item < n + t]
print(f"{out_float} \n")



