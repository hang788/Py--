# 4. 判断列表是否有重复元素。编写一个函数，接受一个列表作为参数，并判断该列表中是否有重复的元素，若有返回True，否则返回False。
# 【输入示例】[1,2,3,4,5,3]
# 【输出示例】True

def func(n):
    b = []
    n = n.replace("[", "")
    n = n.replace("]", "")
    n = n.split(",")
    for i in n:
        b.append(int(i))
    return b


def main():
    str_list = input()
    int_list = func(str_list)
    flag = 0
    for i in int_list:
        if int_list.count(i) != 1:
            flag = 1
            break

    print(True) if flag else print(False)


if __name__ == '__main__':
    main()
