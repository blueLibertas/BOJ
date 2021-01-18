# 문제 출처: https://www.acmicpc.net/problem/1065
# 풀이: 2021.01.18

def check(number):
    return number//100-number//10%10 == number//10%10-number%10

N = int(input())
count = 99 if N > 99 else N
for i in range(100, N+1):
    if check(i):
        count += 1
print(count)