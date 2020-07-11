def my_func():
    print("Hey it's function from module")


if __name__ == '__main__':
    print('Called directly from command line')
else:
    print('Imported as a script with name {}'.format(__name__))
