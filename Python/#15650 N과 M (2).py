# 문제 출처: https://www.acmicpc.net/problem/15650
# 풀이: 2021.02.08

def find(checked, start = 0, answer = []):
    if len(answer) == M:
        for ans in answer:
            print(ans, end = " ")
        print()
        return
    for i in range(start, N):
        if checked[i] == 0:
            checked[i] = 1
            answer.append(i+1)
            find(checked, i+1, answer)
            answer.pop(-1)
            checked[i] = 0


N, M = map(int, input().split())
check = [0 for i in range(N)]
find(check)