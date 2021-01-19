# 문제 출처: https://www.acmicpc.net/problem/2675
# 풀이: 2021.01.19

T = int(input())
for i in range(T):
    R, S = input().split()
    # for letter in S:
    #     print(int(R)*letter, end="")
    # print()
    print("".join([int(R)*x for x in S]))