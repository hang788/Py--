# 9. 字符串分隔打印。获得用户输入的一个字符串（包含空格），将该字符串按照空格分割，并逐行打印。
# 【输入示例】'Python XYU 666'
# 【输出示例】Python
# XYU
# 666

def main():
    str_var = input()
    list_str_var = str_var.split()
    for i in list_str_var:
        print(i)


if __name__ == '__main__':
    main()
