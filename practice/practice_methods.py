# equivalent of built-in all() function
def all(iterable):
    for member in iterable:
        if not member:
            return False
    return True


# equivalent of built-in any() function
def any(iterable):
    for item in iterable:
        if item:
            return True
    return False


# equivalent of built-in enumerate() function
def enumerate(iterable, start=0):
    n = start
    for item in iterable:
        yield n, item
        n += 1

def filter(f, iterable):
    for item in iterable:
        if f(item):
            yield item
        else:
            continue

lst = ['a', 'b', 'c']
for number, item in enumerate(lst, 1):
    print(f"#{number}: {item}")
print('-'*20)
for number, item in enumerate(lst, 1):
    if number > 1:
        break
    else:
        print(f"#{number}: {item}")
print('-'*20)
test_list = [True, 1, 1, 0, 'test']

print(any(test_list))
print(all(test_list))

print('-'*20)
print(list(filter(lambda x: x % 2 == 0, range(20))))
