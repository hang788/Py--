# 5. 计算列表中的平均值。给定一个包含数字的列表，请编写程序来计算列表中所有数字的平均值。
# 【输入示例】[1,2,3,4,5]
# 【输出示例】3
def func(n):
    b = []
    n = n.replace("[", "")
    n = n.replace("]", "")
    n = n.split(",")
    for i in n:
        b.append(int(i))
    return b


def main():
    str_num_list = input()
    int_num_list = func(str_num_list)
    result = sum(int_num_list) / len(int_num_list) * 1.0
    if int(result) == result:
        result = int(result)
    print(result)


if __name__ == '__main__':
    main()
