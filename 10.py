# 10. ⼀球从100⽶⾼度⾃由落下，每次落地后反跳回原⾼度的⼀半，再落下。
# 求它在第10次落地时，共经过多少⽶？第10次反弹多⾼？
# 【输出示例】⼀共经过299.71⽶，第10次反弹的⾼度是0.10。
# （提示：注意字符串的格式化输出）


def fan(n):
    if n == 1:
        return 50
    return fan(n - 1) / 2.0


def main():
    h = 100  # 小球初始的高度
    all_h = 0  # 一共下落的高度
    for i in range(1, 10 + 1):
        all_h += round(fan(i), 3) * 2

    long = fan(10)
    all_h += h - long
    print("⼀共经过{:.5}⽶，第10次反弹的⾼度是{:.1}".format(all_h, long))


if __name__ == '__main__':
    main()
