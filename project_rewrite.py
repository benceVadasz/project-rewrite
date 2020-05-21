def min(x,y):
    less = 0
    numbers = [x,y]
    for num in numbers:
        if x > y:
            less = y
        else:
            less = x
    print(less)
# min(x,y)

x = input("Number 1 ")
y = input("Number 1 ")

def max(x,y):
    greater = 0
    numbers = [x,y]
    for num in numbers:
        if x > y:
            greater = x
        else:
            greater = y
    print(greater)
# max(x,y)

iterable = input(("Write something: "))
def len(iterable):
    lenght = 0
    for sign in iterable:
        lenght +=1
    print(lenght)

# len(iterable)

x = input("Number #1: ")
y = input("Number #2: ")   

def multiply(x,y):
    sum_ = 0
    
    if y > 0:
        counter = 1
        while counter <= y:
            sum_ += x
            counter +=1
    else:
        counter = -1
        while counter >= y:
            sum_ -= x
            counter -=1

    print("result: ", sum_) 
    return sum_

    def power(x,y):
    sum_ = x
    counter = 0
    if y == 0:
        sum_ = 1
        print(sum_)
        return sum_
    elif y > 0:
        while counter < y:
            sum_ *= x
            counter +=1
    elif y < 0:
        while counter > y:
            sum_ = (1/x) * (1/x)
            counter -=1
    print("result: ",sum_)    
    return sum_