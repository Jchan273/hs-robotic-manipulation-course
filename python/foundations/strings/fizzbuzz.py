def fb(n):
    for x in range(1,n+1):
        if (x%3==0) and (x%5==0):
            print("fizzbuzz")
        elif (x%3==0) and not(x%5==0):
            print("fizz")
        elif not(x%3==0) and (x%5==0):
            print("buzz")
        else:
            print(x)

fb(7)
print()
fb(15)