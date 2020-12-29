import random

def gen_fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def gen_squares(n):
    for i in range(n):
        yield i ** 2


def gen_rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


if __name__ == "__main__":
    for num in gen_squares(12):
        print(num)

    print(list(gen_rand_num(5, 15, 10)))

    s = "iteration"
    it = iter(s)
    while True:
        try:
            print(next(it))
        except StopIteration:
            print("Finished!")
            break

    my_list = [1, 2, 3, 4, 5]

    # GENERATOR COMPREHENSION
    gencomp = (item for item in my_list if item > 3)
    print(gencomp)
    for item in gencomp:
        print(item)

