def largest_prime_factor(roof):
    while roof != 1:
        x = 2
        while roof % x != 0:
            x = x + 1
        roof = roof / x
    return x

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))