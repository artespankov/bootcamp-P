import datetime

if __name__ == "__main__":
    # 1 - for..in/else
    # for i in range(10):
    #     print(i)
    #     # if i == 2:
    #     #     break
    # else:
    #     print(f"This will be executed only if no 'break' happened from for..in block")

    # 2 - try/except/else/finally
    # num = int(input("Numerator? "))
    # denom = int(input("Denominator? "))
    # try:
    #     res = num / denom
    # except ZeroDivisionError:
    #     print('ZERO DIVISION FOOL')
    # except Exception:
    #     print('whatevererror')
    # else:
    #     print('It\'s okay, no errors')
    # finally:
    #     print('All done for today')

    # 3 string.isdigit()
    # print("ABC".isdigit())
    # print("1000".isdigit())
    # print("-13".isdigit()) # note that it doesn't work with negatives

    x = {1, 2, 3}
    y = 2
    z = 3

    import pdb
    result = y + z
    pdb.set_trace()
    result2 = x + y
    pdb.set_trace()
