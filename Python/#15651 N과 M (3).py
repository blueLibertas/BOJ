# 문제 출처: https://www.acmicpc.net/problem/15651
# 풀이: 2021.02.08

def find(answer = []):
    if len(answer) == M:
        for ans in answer:
            print(ans+1, end = " ")
        print()
        return
    for i in range(N):
        answer.append(i)
        find(answer)
        answer.pop(-1)


N, M = map(int, input().split())
find()