# 문제 출처: https://www.acmicpc.net/problem/8958
# 풀이: 2021.01.18

T = int(input())
for i in range(T):
    answer = input()
    score = cummulative = 0
    for ans in answer:
        if ans == "O":
            cummulative += 1
            score += cummulative
        else:
            cummulative = 0
    print(score)
