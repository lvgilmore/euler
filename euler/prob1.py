def count_multiples(roof, multipliers):
    sum = 0
    for i in range(1, roof):
        flag = True
        for j in multipliers:
            if flag and i%j == 0:
                sum = sum + i
                flag = False
    return sum

if __name__ == '__main__':
    print(count_multiples(1000, [3, 5]))
