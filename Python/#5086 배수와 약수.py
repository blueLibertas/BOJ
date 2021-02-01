# 문제 출처: https://www.acmicpc.net/problem/5086
# 풀이: 2021.02.01

def factorOrMultiple(A, B):
    if A % B == 0:
        return "multiple"
    elif B % A == 0:
        return "factor"
    return "neither"

A, B = map(int, input().split())
while A != 0 and B!= 0:
    print(factorOrMultiple(A, B))
    A, B = map(int, input().split())
