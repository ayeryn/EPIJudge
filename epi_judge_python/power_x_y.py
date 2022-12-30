from test_framework import generic_test


def power_brute(x: float, y: int) -> float:
    """
    Take a double -x, and an integer - y, and returns x**y
    O(2^n) : n is the number of bits needed to represent y
    """
    for i in range(y):
        x *= x
    return x

# To improve, increase the amount of multiplications done at each step
# See notes for details


def calc(x: float, y: int) -> float:
    """
    Actual calculation function
    Defines base cases of y = 0 or 1
    o.w. use exponential property to calculate each step
    """
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2:
        # y is odd
        return power(x, y//2) * power(x, y//2) * x
    else:
        # y is even
        return power(x, y//2) * power(x, y//2)


def power_helper(x: float, y: int) -> float:
    """
    Use abs(y) to calculate the exponential component
    Inverse if necessary before return based on actual y
    """
    ret = calc(x, abs(y))
    if y < 0:
        return 1/ret
    else:
        return ret


def power_int(x: float, y: int) -> float:
    """
    Integer arithmetic implementation
    """
    if y < 0:
        y = abs(y)
        x = 1/x

    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2:
        # y is odd
        return power(x, y//2) * power(x, y//2) * x
    else:
        # y is even
        return power(x, y//2) * power(x, y//2)


def power(x: float, y: int) -> float:
    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
