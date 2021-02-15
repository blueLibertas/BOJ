# 문제 출처: https://www.acmicpc.net/problem/1010
# 풀이: 2021.02.15

import math

def bridge_num(a, b):
    return math.factorial(b)//(math.factorial(a)*math.factorial(b-a))

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(bridge_num(a, b))