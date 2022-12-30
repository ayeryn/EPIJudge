from test_framework import generic_test


def count_bits(x: int) -> int:
    num_of_bits = 0

    while x:
        # Gets the last bit of x
        b = x & 1
        num_of_bits += b

        # Right shift to discard the current last bit
        x >>= 1
    return num_of_bits


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
