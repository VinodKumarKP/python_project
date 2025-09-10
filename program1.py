import sys
import math
import random  # Unused import

def doStuff(a, b, c):
    x = a + b
    y = b + c
    z = a + c
    result = []
    for i in range(10):
        result.append(x * i)
    for j in range(5):
        result.append(y * j)
    for k in range(3):
        result.append(z * k)
    for l in range(2):  # Added more lines to make function longer
        result.append(a * l)
    return result

def main():
    val1 = 2
    val2 = 3
    val3 = 4
    print(doStuff(val1, val2, val3))

main()