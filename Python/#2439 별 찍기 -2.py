# 문제 출처: https://www.acmicpc.net/problem/2439
# 풀이: 2021.01.16

N = int(input())
for i in range(N):
    temp = "{:>"+str(N)+"}"
    print(temp.format("*"*(i+1)))