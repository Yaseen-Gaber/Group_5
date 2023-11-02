array = [10, 20, 30, 40, 50]

print(array)
# print(array[3])

Length = len(array)
print(Length)

'''
for i in range(0, len(array)):
    print(array[i], end= " ")
'''

array.append(88)
print(array)
print(len(array))

# overwriting an index value in an array
array[0] = 100

print(array)


#################################################################################################################################################

import array as arr

# declare an array

# array1 = arr.array('i', [10, 20, 30, 40, 50])

# Length = len(array1)
# print(Length)

# for i in range(0, Length):
#     print(array1, i)

# array1.insert(5, 80)

# for i in range(0, Length):
#     print(array1[i], end= " ")

# removing an element from an array

# array1.remove(array1[1])

# Length = len(array1)
# print("\n")

# arrayNP = []

# for i in range(0, Length):
#     arrayNP.append(0)

# print(arrayNP)

# Printing the decimal numbers tpye of array using while loop

"""
c = [-10, -20, +30, -40, -50]
array1 = arr.array('d', c)

index = 0
while index < len(array1):
    print(array1[index])
    index += 1
"""

# import random

# random.seed(1)  # I have no idea wtf "seed" is, so go f**king YT it

# array = [random.randint(0, 10)]
# for i in range(5):
#     print(array)

def even_only_loop(string):
    evens = ""
    while string != "":
        evens += string[0]
        string = string[2:]
    return evens

def main():
    returnedEvens = even_only_loop("abcdefghijk")
    print(returnedEvens)

main()