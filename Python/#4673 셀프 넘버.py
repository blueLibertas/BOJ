# 문제 출처: https://www.acmicpc.net/problem/4673
# 풀이: 2021.01.18

until = 10000
number_list = [x for x in range(1, until+1)]

def check_recursive(number):
    if number > until or number not in number_list:
        return
    d = number + sum([int(x) for x in str(number)])
    if d in number_list:
        check_recursive(d)
        number_list.remove(d)

def check_one(number):
    if number > until:
        return
    d = number + sum([int(x) for x in str(number)])
    if d in number_list:
        number_list.remove(d)

for i in range(until):
    check_recursive(i)
    # check_one(i)

for element in number_list:
    print(element)
