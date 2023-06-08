# 1. 回文数判断。设n是一任意自然数，如果n的各位数字反向排列所得自然数与n相等，
# 则n被称为回文数。从键盘输入一个数字，请编写程序判断这个数字是不是回文数，若是返回True，否则返回False。
# 【输入示例】12321
# 【输出示例】True
def main():
    n = input()
    print(False) if n != n[::-1] or n[-1] == 0 and n != "0" else print(True)


if __name__ == '__main__':
    main()
