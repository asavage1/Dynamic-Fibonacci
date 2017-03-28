"""
fib_memo.py
Andrew Savage
3/28/17

Calculate the nth fibonacci number, recursively, using memoization
n is input using command line arguments
"""

import sys

def main(n):
    lookup_table = [0, 1] #1st and 2nd fib numbers are 0 and 1, respectively
    print find_nth(n, lookup_table)
    return 0

def find_nth(n, lt):
    if len(lt) > n:
        return lt[n]
    num = find_nth(n - 1, lt) + find_nth(n - 2, lt)
    lt.append(num)
    return num

main(int(sys.argv[1]))
