from collections import Counter


def break_to_primes(x):
    primes = []
    while x > 1:
        i = 2
        while x % i != 0:
            i = i + 1
        x = x / i
        primes.append(i)
    return primes


def get_all_primes(floor, roof):
    primes = Counter([])
    for i in range(floor, roof):
        primes = primes + (Counter(break_to_primes(i)) - primes)
    return primes


def minimum_multipliers(floor, roof):
    multiplier = 1
    primes = get_all_primes(floor, roof)
    print("{}\n".format(primes))
    for prime, qunatity in primes.iteritems():
        multiplier = multiplier * pow(prime, qunatity)
    return multiplier

if __name__ == '__main__':
    print(minimum_multipliers(1, 20))
