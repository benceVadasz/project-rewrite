x = input("Number 1: ")
y = input("Number 2: ")
def mini(x,y):
    more = 0
    numbers = [x,y]
    for num in numbers:
        if x > y:
            more = x
        else:
            more = y
    print(more)
mini(x,y)