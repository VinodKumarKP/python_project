# remediation_issue_big.py
import sys
import math

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
    return result

def main():
    val1 = 2
    val2 = 3
    val3 = 4
    print(doStuff(val1, val2, val3))

main()