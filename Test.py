def function_b(b_list, high_num):
    c_list = [0, 0, 0, 0, 0, 0,0]
    i = 0
    for num in b_list:
        if num > high_num:
            c_list[i] = num
        i = i + 1
    b_list = c_list
    return b_list

def main():
    b_list = [1,3, 6, 4, 1, 2, 8]
    high_num = 4
    function_b(b_list, high_num)
    print(b_list)

main()