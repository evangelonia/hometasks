"""Make a function that takes an integer (in decimal form)
and convert it to a binary form using recursion  """


def to_binary_func(n):
    res, ost = n % 2, n // 2
    if ost in [1, 0]:
        print(res, ost)
        return f"{ost}{res}"
    print(res)
    return to_binary_func(ost) + str(res)


print(to_binary_func(int(input("Введите число:"))))
