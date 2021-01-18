# 문제 출처: https://www.acmicpc.net/problem/4344
# 풀이: 2021.01.18

T = int(input())
for i in range(T):
    scores = list(map(int, input().split()))[1:]
    avg = (sum(scores))/(len(scores))
    count = 0
    for item in scores:
        if item > avg:
            count += 1
    print("{:.3f}%".format(count/len(scores)*100))