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


collection = [1, 4, 2, 1, 2, 7, 8, 1, 3, 7, 9]


def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print(Repeat(collection))
