# 문제 출처: https://www.acmicpc.net/problem/1011
# 풀이: 2021.01.23 ~ 24

import math

def calc_movement(length):
    n = math.sqrt(length)
    n_floor = math.floor(n)
    if n == n_floor:
        return 2*n_floor -1
    if length <= n_floor * (n_floor+1):
        return 2*n_floor
    return 2*n_floor+1

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    print(calc_movement(y-x))
