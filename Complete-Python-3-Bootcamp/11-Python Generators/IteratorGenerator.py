class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        if x > 2:
            raise StopIteration("We can count up to 2 only")
        self.a += 1
        return x


def desc_generator(val):
    while val > 5:
        val -= 1
        yield val
    else:
        return "Can't count up the negative amount of items"


if __name__ == '__main__':
    from builtins import range
    nums = MyNumbers()
    my_iterator = iter(nums)
    # stop when iterator exhausted
    for i in my_iterator:
        print(i)
    gen_iter = desc_generator(-15)
    print(next(gen_iter))
    for i in gen_iter:
        print(i)

    # will raise the StopIteration
    gen_iter = desc_generator(-15)

