def exchange_values_without_third_variable():
    x = 10
    y = 5

    print("x: {0}, y: {1}".format(x, y))
    # x = x ^ y
    # y = y ^ x
    # x = x ^ y

    x = x + y
    y = x - y
    x = x - y

    print("x: {0}, y: {1}".format(x, y))


exchange_values_without_third_variable()
