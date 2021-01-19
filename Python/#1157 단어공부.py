# 문제 출처: https://www.acmicpc.net/problem/1157
# 풀이: 2021.01.19

word = input().upper()
letters = set([x for x in word])
if len(letters)==1:
    print(letters.pop())
else:
    count = []
    for letter in letters:
        count.append([word.count(letter), letter])
    count.sort(reverse=True)
    print(count[0][1] if count[0][0] != count[1][0] else "?")