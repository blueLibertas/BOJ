# 문제 출처: https://www.acmicpc.net/problem/9020
# 풀이: 2021.01.27

def goldbach(number):
    half = number//2
    while True:
        if half in prime and number-half in prime:
            print(half, number-half)
            return
        half -= 1

End = 10000
prime = []
check = [True] * (End+1)

for i in range(2, End+1):
    if (check[i]):
        prime.append(i)
        for j in range(End//i+1):
            check[i*j] = False

T = int(input())
for i in range(T):
    goldbach(int(input()))
