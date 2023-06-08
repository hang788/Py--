# 12. 给你两个整数a和b（-10000<a,b<10000），请你判断是否存在两个整数，他们的和为a，乘积为b。
# 若存在，输出Yes,否则输出No。
# 【输入示例】a=9,b=15
# 【输出示例】No

# 设两个整数为x，y，则x+y=a，x*y=b，即x+b/x=a,x**2-a*x+b=0
# 因此只需判断此时x的值是否存在且为整数即可
def func(a, b):
    de_ta = a ** 2 - 4 * b
    if de_ta < 0:
        return "No"
    x1 = (a + de_ta ** 0.5) / 2.0
    x2 = (a - de_ta ** 0.5) / 2.0
    if x1 == int(x1) and x2 == int(x2):
        return "Yes"
    else:
        return "No"


def main():
    a = int(input("请输入整数a的值"))
    b = int(input("请输入整数b的值"))
    print(func(a, b))


if __name__ == '__main__':
    main()
