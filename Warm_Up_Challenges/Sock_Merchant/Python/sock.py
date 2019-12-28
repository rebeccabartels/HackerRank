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
        return n


input()
socks = input().strip().split()
pairs = 0

for element in set(socks):
    pairs += socks.count(element) // 2
print(pairs)


# print(Repeat(collection))
