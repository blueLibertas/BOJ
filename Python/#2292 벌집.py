# 문제 출처: https://www.acmicpc.net/problem/2292
# 풀이: 2021.01.22

import math

def count(dest):
    if dest == 1:
        return 1
    k = math.floor(math.sqrt((dest-1)/3))
    if dest > 1+3*(k+1)*k:
        k += 1
    return k+1

print(count(int(input())))
