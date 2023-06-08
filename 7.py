# 7. 统计字符串中的元音字母个数。从键盘输入一串字符串，统计该字符串中元音字母（a、e、i、o、u）的个数。
# 【输入示例】'abe'
# 【输出示例】2

def main():
    str_var = input()
    yuan_yin = ["a", "e", "i", "o", "u"]
    count = 0
    for i in yuan_yin:
        count += str_var.count(i)
    print(count)


if __name__ == '__main__':
    main()
