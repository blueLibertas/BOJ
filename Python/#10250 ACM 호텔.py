# 문제 출처: https://www.acmicpc.net/problem/10250
# 풀이: 2021.01.14

T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())

    floor = H if N % H == 0 else N % H
    num = N // H if N % H == 0 else N // H+ 1

    print('{}{:02d}'.format(floor, num))
