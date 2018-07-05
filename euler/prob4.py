def is_palindrome(x):
    x = str(x)
    flag = True
    for i in range(0, len(x)/2):
        if x[i] != x[-i-1]:
            flag = False
    return flag


def does_divide(x, roof, floor):
    for i in range(roof, floor+(roof-floor)/2, -1):
        if x % i == 0 and roof >= x / i >= floor:
            print("i: {}, x/i: {}".format(i, x/i))
            return True
    return False


def largest_multiply_palindrome(roof, floor):
    x = roof * roof
    flag = True
    while flag:
        if is_palindrome(x) and does_divide(x, roof, floor):
            flag = False
        else:
            x = x - 1
    return x

if __name__ == '__main__':
    print(largest_multiply_palindrome(999, 100))
