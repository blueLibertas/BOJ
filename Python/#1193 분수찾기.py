# 문제 출처: https://www.acmicpc.net/problem/1193
# 풀이: 2021.01.14

import math
nth = int(input())
""" 
주의점: 순서가 지그재그!!
X가 A번째 그룹, B번쨰 숫자라고 하면 
a(a-1)/2 < X <= a(a+1)/2
a-1 < sqrt(2X) < a+1
A = a-1 또는 a
"""

A = math.floor(math.sqrt(nth*2))
if nth > A*(A+1)/2:
    A += 1
until_A = int(A*(A-1)/2)
if A % 2 == 0:
    B = nth - until_A
else:
    B = A+1-nth+until_A

# print('A:{} until_A:{} B:{}'.format(A, until_A, B))
print('{}/{}'.format(B, A+1-B))
