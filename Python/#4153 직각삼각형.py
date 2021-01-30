# 문제 출처: https://www.acmicpc.net/problem/4153
# 풀이: 2021.01.30

A, B, C = map(int, input().split())
while A!= 0 and B != 0 and C != 0:
    if A*A + B*B == C*C or A*A + C*C == B*B or B*B + C*C == A*A:
        print("right")
    else:
        print("wrong")
#    print("right" if A * A + B * B == C * C or A * A + C * C == B * B or B * B + C * C == A * A else "wrong")
    A, B, C = map(int, input().split())