# 문제 출처: https://www.acmicpc.net/problem/3052
# 풀이: 2021.01.18

remainder = set()
for i in range(10):
    remainder.add(int(input())%42)
print(len(remainder))