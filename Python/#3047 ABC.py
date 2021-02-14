# 문제 출처: https://www.acmicpc.net/problem/3047
# 풀이: 2021.02.14

def find(letter):
    if letter == "A":
        return numbers[0]
    elif letter == "B":
        return numbers[1]
    return numbers[2]

numbers = [int(x) for x in input().split()]
numbers.sort()
order = input()
for i in range(3):
    print(str(find(order[i])), end=" ")
# result = ''
# for i in range(3):
#     result += str(find(order[i]))+ " "
# print(result)
