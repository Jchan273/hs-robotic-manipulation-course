from math import pi

def main():
    """
    Print some facts about a circle with radius 10.
    """
    radius = 10
    area = round(pi*(radius**2),2)
    cir = 2*pi*radius
    print(area, cir)

if __name__ == '__main__':
    main()
