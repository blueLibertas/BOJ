# 문제 출처: https://www.acmicpc.net/problem/15652
# 풀이: 2021.02.09

def find(start = 0, answer = []):
    if len(answer) == M:
        for ans in answer:
            print(ans, end = " ")
        print()
        return
    for i in range(start, N):
        answer.append(i+1)
        find(i, answer)
        answer.pop(-1)


N, M = map(int, input().split())
check = [0 for i in range(N)]
find()