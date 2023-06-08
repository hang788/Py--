# 2. 素数判断。编写一个函数isPrime(x)，接受一个正整数作为参数，并判断该数是否为素数（只能被1和自身整除）,若是返回True，否则返回False。
# 【输入示例】3
# 【输出示例】True

def isPrime(x):
    for i in range(2, int(pow(x, 0.5)) + 1):
        if x % i == 0:
            return False
    return True


def main():
    n = int(input())
    print(isPrime(n))


if __name__ == '__main__':
    main()
