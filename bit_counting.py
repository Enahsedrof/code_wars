def  count_bits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count