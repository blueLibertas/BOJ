# 문제 출처: https://www.acmicpc.net/problem/11653
# 풀이: 2021.01.23

N = int(input())

for i in range(2, N//2):
    while N % i == 0:
        print(i)
        N = N // i
if N != 1:
    print(N)