#!/usr/bin/python3
import sys

def strAssign(str, idx, char):
    if idx == 0:
        return char + str[1:]
    elif idx == len(str)-1:
        return str[0:idx] + char
    else:   
        return str[0:idx] + char + str[idx+1:]


def judge2A2B(ans, quess):
    a_num = 0
    b_num = 0
    tmp_a = [0 for _ in range(4)]
    tmp_b = [0 for _ in range(4)]

    for i in range(0, 4) :
        if ans[i] == quess[i] :
            a_num = a_num + 1
            tmp_a[i] = 1

    for i in range(0, 4) : 
        for j in range(0, 4) :
            if tmp_a[i] == 1 :
                break
            t = quess.find(ans[i], j)
            if tmp_a[i] == 0 and tmp_b[j] == 0 and t > -1 : 
                tmp_b[t] = 1
                b_num = b_num +1
                break 

    return a_num, b_num

#ans = input('Please input 4 digits number : ')
ans = '1221'
a = 0

while (a != 4) :
    guess = input('Please input your guess : ')
    a, b =  judge2A2B(ans, guess)
    print('{}A{}B'.format(a, b))