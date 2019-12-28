import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        n = int(input())
        ar = list(map(int, input().rstrip().split()))
        result = sockMerchant(n, ar)
        fptr.write(str(result) + '\n')
        fptr.close()


collection = [1, 1, 2, 3, 2, 4, 4, 1, 3]


def func():
    pairs = 0
    totalsingles = len(collection)
    print(totalsingles)
    bucket = []
    for sock in collection:
        print(sock)
        bucket.append(sock)
        print(bucket)
        dups = [sock for sock in collection if collection.count(sock) > 1]
        print("These are the dups: " + str(dups))


func()
