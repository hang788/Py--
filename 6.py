# 6. 反转整数。编写一个函数，接受一个整数作为参数，并返回该整数的反转形式。
# 【输入示例】123
# 【输出示例】321

def func(n):
    return int(str(n)[::-1])


def main():
    a = int(input())
    print(func(a))


if __name__ == '__main__':
    main()
