from test_framework import generic_test


def parity_brute(x: int) -> int:
    """
    Brute-force implementation
    O(n)
    """
    p = 0
    while x:
        # Process each bit from lowest bit
        if x & 1:
            p += 1
        x >>= 1
    return p % 2


def parity_k(x: int) -> int:
    """
    x & (x-1) = x with the lowest **set** bit removed
    O(k) : k is the number of set bits
    """
    p = 0
    while x:
        p ^= 1
        x &= x-1

    return p


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
