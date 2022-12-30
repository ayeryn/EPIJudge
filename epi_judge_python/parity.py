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
        # Flips p every time to keep track of odd/evenness
        p ^= 1
        # Drops to the lowest set bit of x
        x &= x-1

    return p

# def parity_cache(): break into parts and cache the first x entries


def parity(x: int) -> int:
    # Every round do: (higher half XOR lower half)
    # The higher half will preserve, BUT
    # only the lowest bit will be observed at the end
    # See notes for detailed explanation
    x = x ^ (x >> 32)
    x = x ^ (x >> 16)
    x = x ^ (x >> 8)
    x = x ^ (x >> 4)
    x = x ^ (x >> 2)
    x = x ^ (x >> 1)

    # Ignore leading 0s
    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
