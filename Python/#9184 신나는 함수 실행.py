# 문제 출처: https://www.acmicpc.net/problem/9184
# 풀이: 2021.02.11

w = [[[1 for i in range(21)] for i in range(21)] for i in range(21)]
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j < k:
                w[i][j][k] = w[i][j][k - 1] + w[i][j - 1][k - 1] - w[i][j - 1][k]
            else:
                w[i][j][k] = w[i - 1][j][k] + w[i - 1][j - 1][k] + w[i - 1][j][k - 1] - w[i - 1][j - 1][k - 1]


def recursive_function(a, b, c):
    if a < 1 or b < 1 or c < 1:
        return w[0][0][0]
    if a > 20 or b > 20 or c > 20:
        return w[20][20][20]
    return w[a][b][c]


a, b, c = map(int, input().split())
while not a == b == c == -1:
    result = recursive_function(a, b, c)
    print("w({}, {}, {}) = {}".format(a, b, c, result))
    a, b, c = map(int, input().split())
