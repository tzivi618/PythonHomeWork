import datetime


def run_time(func):
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        # return end - start
        print(end - start)

    return inner


# 2
dic = {}


def cache(func):
    def inner(n):
        if dic.keys().__contains__(n):
            print(dic[n])
            return dic[n]
        else:
            num = func(n)
            dic[n] = num
            print(num)
            return num
    return inner


@run_time
def print_numbers(n):
    for i in range(n):
        print(f'{i}')


FibArray = [0, 1]


@run_time
@cache
def fibonacci(n):
    num1 = 0
    num2 = 1
    for _ in range(n - 1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    return num3


print(fibonacci(100))
