# 문제 출처: https://www.acmicpc.net/problem/2869
# 풀이: 2021.01.11 

import math
a, b, v = map(int, input().split())
print(math.ceil((v-a)/(a-b))+1)