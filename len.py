iterable = input(("Enter something: "))
def len(iterable):
    lenght = 0
    for sign in iterable:
        lenght +=1
    print(lenght)

len(iterable)