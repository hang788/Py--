# 11. 给定两个正整数a, b (1<=a <= b<=10^5), 请你数出在a到b之间，十个阿拉伯数字分别出现了多少次。
# 比如，当a=11, b=20时，a和b之间的数有[11,12,13,14,15,16,17,18,19,20]，
# 那么0-9这10个数出现的次数分别是1,10,2,1,1,1,1,1,1,1。
# 现在给你a和b，请你输出十个阿拉伯数字分别出现的次数；
# 分十行输出，第一行表示0出现的次数，第二行表示1出现的次数，....,最后一行表示9出现的次数。
# 【输入示例】a =11,b =20
# 【输出示例】1, 10, 2, 1, 1, 1, 1, 1, 1, 1（按行输出）

def main():
    a = int(input("输入a的值"))
    b = int(input("输入b的值"))
    dir_count = {}
    for i in range(a, b + 1):
        str_num = str(i)
        for j in range(len(str_num)):
            str_num_j = str_num[j]
            dir_count[str_num_j] = dir_count.get(str_num_j, 0) + 1
    item = list(dir_count.items())
    item.sort(key=lambda x: x[0])
    for i in item:
        print(i[1])


if __name__ == '__main__':
    main()
