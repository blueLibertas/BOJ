# 문제 출처: https://www.acmicpc.net/problem/1002
# 풀이: 2021.01.30

import math
T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)**2+(y1-y2)**2)

    # 같은 원이라 접점이 무한개
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    # 만나지 않을 경우
    elif r1+r2 < d or abs(r1-r2) > d:
        print(0)
    elif r1+r2 == d or abs(r1-r2) == d:
        print(1)
    else:
        print(2)