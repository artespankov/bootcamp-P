def decorator(original_f):

    def wrapper(a, b):
        print("Some staff before the func!")
        original_f(a, b)
        print("Some staff after the func!")
    return wrapper


if __name__ == "__main__":
    @decorator
    def calc(a, b): print(a+b)


    calc(111, 111)
