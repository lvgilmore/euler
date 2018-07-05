def find_next_prime(primes):
    x = primes[-1] + 1
    flag = True
    while flag:
        flag = False
        for p in primes:
            if x % p == 0:
                flag = True
                break
        if flag:
            x = x + 1
        else:
            break
    return x


def find_xth_prime(x):
    primes = [2]
    for i in range(1, x):
        primes.append(find_next_prime(primes))
    return primes[-1]


if __name__ == '__main__':
    print(find_xth_prime(10001))
