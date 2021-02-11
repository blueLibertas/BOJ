# 문제 출처: https://www.acmicpc.net/problem/1003
# 풀이: 2021.02.11

fibb_zero = [1, 0]
fibb_one = [0, 1]
for i in range(2, 41):
    fibb_zero.append(fibb_zero[i-1] + fibb_zero[i-2])
    fibb_one.append(fibb_one[i-1] + fibb_one[i-2])

T = int(input())

for i in range(T):
    N = int(input())
    print(fibb_zero[N], fibb_one[N])