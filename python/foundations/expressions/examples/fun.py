def add_3_mul_4(num):
    """
    Add 3 to the num, then multiply by 4.

    >>> add_3_mul_4(2)
    20
    """
    num+=3
    num*=4
    return num
    
def calc_area(length=1,width=1):
    """
    Compute the area of a rectangle
    >>> calc_area()
    1

    >>> calc_area(3)
    3

    >>> calc_area(12,3)
    36
    """


    print("Calculating area of the rectangle...")
    return length * width