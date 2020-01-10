arr = [4,5,734,43]

#Your code go here:
def sumOdds():
    aux=0
    for i in arr:
        if i % 2 == 1:
            aux += i
    print(aux)


sumOdds()
