# 문제 출처: https://www.acmicpc.net/problem/2309
# 풀이: 2021.02.16

def find_false():
    for i in range(9):
        for j in range(9):
            if i != j and all - height[i] - height[j] == 100:
                height[i] = height[j] = 100
                return

height = []
for i in range(9):
    height.append(int(input()))
all = sum(height)
find_false()

height.sort()
for i in range(7):
    print(height[i])