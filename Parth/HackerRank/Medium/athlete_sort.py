import math
import os
import random
import re
import sys

def athlete_sort(arr, k):

    result_arr = sorted([val for val in arr], key=lambda x: x[k])

    for i in result_arr:
        print(*i, sep=', ')

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    print(athlete_sort(arr, k))
