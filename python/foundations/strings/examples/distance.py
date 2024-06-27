import math

def main():
    """
    Prompt the user to input the coordinates of two points (x1, y1) and (x2, y2).
    Then, compute the distance using the formula:

        √((x2 - x1)^2 + (y2 - y1)^2)

    Example:
    --------
    Enter x_1: 1
    Enter x_2: 4
    Enter y_1: 2
    Enter y_2: 6
    The distance between the points (1, 2) and (4, 6) is 5.0
    """
    x1 = int(input("Enter x_1: "))
    y1 = int(input("Enter y_1: "))
    x2 = int(input("Enter x_2: "))
    y2 = int(input("Enter y_2: "))

    print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {math.sqrt((x2-x1)**2+(y2-y1)**2)}")

main()