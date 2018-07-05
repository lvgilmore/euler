def count_even_fibonachy(roof, s1, s2):
    x = 0
    x = x + s1 if s1 % 2 == 0 and s1 < roof else x
    x = x + s2 if s2 % 2 == 0 and s2 < roof else x
    while s1 < roof and s2 < roof:
        s1 = s1 + s2
        s2 = s1 + s2
        x = x + s1 if s1 % 2 == 0 and s1 < roof else x
        x = x + s2 if s2 % 2 == 0 and s2 < roof else x
    return x

if __name__ == '__main__':
    print(count_even_fibonachy(4000000, 1, 2))
