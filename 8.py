# 8. 统计水仙花数。“水仙花数”是指一个三位数中各个数位上数字的立方和等于该数本身。
# 例如153是一个水仙花数，因为153=13+53+33。
# 编写程序，计算200到500之间的水仙花数共有多少个。

def sui_xian(n):
    str_n = str(n)
    num = 0
    for i in str_n:
        num += int(i) ** 3
    return num == n


def main():
    count = 0
    for i in range(200, 500 + 1):
        if sui_xian(i):
            count += 1
    print(count)


if __name__ == '__main__':
    main()
