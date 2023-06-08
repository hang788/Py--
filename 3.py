# 3. 统计字母出现次数。编写一个函数，接受一个字符串作为参数，并统计每个字母出现的次数，
# 然后返回一个字典，字典的键为字母，值为出现的次数。
# 【输入示例】'abb'
# 【输出示例】{'a': 1, 'b': 2}

def func(n):
    dir_str = {}
    for i in n:
        dir_str[i] = dir_str.get(i, 0) + 1
    return dir_str


def main():
    str_var1 = input()
    print(func(str_var1))


if __name__ == '__main__':
    main()
