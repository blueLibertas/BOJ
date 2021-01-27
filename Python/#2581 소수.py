# 문제 출처: https://www.acmicpc.net/problem/2581
# 풀이: 2021.01.27

Start = int(input())
End = int(input())
prime = []
check = [True] * (End+1)

for i in range(2, End+1):
    if (check[i]):
        if i >= Start:
            prime.append(i)
        for j in range(End//i+1):
            check[i*j] = False

print("{}\n{}".format(sum(prime), min(prime))) if prime else print(-1)
