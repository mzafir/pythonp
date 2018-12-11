def findtrapwater(RainList):
    l_index = 0
    r_index = len(RainList) - 1
    right_max = 0
    left_max = 0
    f_answer=0
    while l_index < r_index:
        if RainList[l_index] > RainList[r_index]:
            if RainList[l_index] > left_max or RainList[l_index] == left_max:
                left_max = RainList[l_index]
                l_index=l_index+1
        else:
            f_answer = f_answer+left_max - RainList[l_index]
            l_index = l_index + 1
    else:

        if RainList[r_index] > right_max:
            right_max = RainList[r_index]
            r_index=r_index-1
        else:
            f_answer = f_answer + right_max - RainList[r_index]
            r_index = r_index - 1

    return f_answer

a=[7,1,4,0,2,8,6,3,5]

print(findtrapwater(a))
