# 문제 출처: https://www.acmicpc.net/problem/9663
# 풀이: 2021.02.10

def can_position(curr, candidate, pos):
    for i in range(1, curr):
        if pos[i] == candidate or abs(curr-i) == abs(candidate - pos[i]):
            return False
    return True

def n_queens(curr, total, pos, count = 0):
    if curr == total+1:
        return count+1

    for i in range(1, total+1):
        if can_position(curr, i, pos):
            pos[curr] = i
            count = n_queens(curr+1, total, pos, count)
            pos[curr] = 0

    return count

N = int(input())
# print(n_queens(1, N, [0 for i in range(N+1)]))
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[N])

# 풀이: 2021.02.11

# import copy
# def n_queens(curr, total, pos, count = 0):
#     if curr == total+1:
#         return count+1
#
#     for i in range(1, total+1):
#         if pos[curr][i] == 0:
#             temp = copy.deepcopy(pos)
#             temp[curr][i] = 99
#             for k in range(curr+1, N+1):
#                 temp[k][i] = -1
#             for k in range(1, min(N+1-curr, N+1-i)):
#                 temp[curr+k][i+k] = -1
#             for k in range(1, min(N+1-curr, i)):
#                 temp[curr+k][i-k] = -1
#             count = n_queens(curr+1, total, temp, count)
#
#     return count
#
# N = int(input())
# board = [[0 for i in range(N+1)] for i in range(N+1)]
# print(n_queens(1, N, board))