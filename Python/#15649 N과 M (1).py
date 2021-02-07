# 문제 출처: https://www.acmicpc.net/problem/15649
# 풀이: 2021.02.07

def find(checked, answer = []):
    if len(answer) == M:
        for ans in answer:
            print(ans+1, end = " ")
        print()
        return
    for i in range(N):
        if checked[i] == 0:
            checked[i] = 1
            answer.append(i)
            find(checked, answer)
            answer.pop(-1)
            checked[i] = 0


N, M = map(int, input().split())
check = [0 for i in range(N)]
find(check)