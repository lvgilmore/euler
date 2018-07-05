def square_sum(rng):
    sum = 0
    for i in rng:
        sum = sum + pow(i, 2)
    return sum


def sum_square(rng):
    return pow(sum(rng), 2)


if __name__ == '__main__':
    rng = range(1, 101)
    print("{}\n{}\n".format(sum_square(rng), square_sum(rng)))
    print(sum_square(rng) - square_sum(rng))
