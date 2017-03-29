"""
fib_bottomup.py
Andrew Savage
3/28/17

Calculate the nth fibonacci number, recursively, using the bottom up approach
n is input using command line arguments
"""

import sys

def main(n):
    lookup_table = [0, 1] #1st and 2nd fib numbers are 0 and 1, respectively
    print find_nth(n, lookup_table)
    return 0

def find_nth(n, lt):
    while len(lt) <= n:
        lt.append(lt[len(lt) - 1] + lt[len(lt) - 2])
    return lt[n]

main(int(sys.argv[1]))
