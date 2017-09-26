def factor_count(num):
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count += 1
    return count
