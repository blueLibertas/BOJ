# 문제 출처: https://www.acmicpc.net/problem/1316
# 풀이: 2021.01.19

def check(word):
    letters = set()
    prev = ""

    for letter in word:
        if prev == letter:
            continue
        elif letter in letters:
            return 0
        else:
            prev = letter
            letters.add(letter)
    return 1


T = int(input())
count = 0
for i in range(T):
    count += check(input())
print(count)