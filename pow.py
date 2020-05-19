def pow(x, y):
    x = int(input("Number #1: "))
    y = int(input("Number #2: "))
    a = 1
    z = 1
    for a in range (y):
        z = z * x
    print(z)
    return
pow(3, 8)