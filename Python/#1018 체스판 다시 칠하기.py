# 문제 출처: https://www.acmicpc.net/problem/1018
# 풀이: 2021.02.03
def check_line(input_line, nth_line, A):
    compare = "WBWBWBWB" if (A == "W" and nth_line%2==0) or (A == "B" and nth_line%2 != 0) else "BWBWBWBW"
    count = 0
    for i in range(8):
        if compare[i] != input_line[i]:
            count += 1
    return count

def check_recolor_tiles(start_X, start_Y, A, B):
    count = 0
    for i in range(start_X, start_X+8):
        count += check_line(board[i][start_Y:start_Y+8],i, A)
    return count

N, M = map(int, input().split())
recolor = 65
board = []
for i in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        recolor = min(recolor, check_recolor_tiles(i, j, 'B', 'W'), check_recolor_tiles(i, j, 'W', 'B'))
print(recolor)
