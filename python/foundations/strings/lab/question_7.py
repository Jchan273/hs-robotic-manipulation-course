def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    count=1
    for x in range(k):
        count*= n
        n-=1
    print(count)

falling(6,3)
falling(4,3)
falling(4,1)
falling(4,0)