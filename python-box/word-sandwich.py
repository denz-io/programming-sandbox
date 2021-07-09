def flatten(NestedArray):
    if NestedArray == []:
        return NestedArray
    if isinstance(NestedArray[0], list):
        return flatten(NestedArray[0]) + flatten(NestedArray[1:])
    return NestedArray[:1] + flatten(NestedArray[1:])

def unwrap(sandwich, se, wordLength):
    import random
    Random = random.sample(se, 1)
    Spread = Random[0]

    if(sandwich.find(Spread) != -1):
        Loafs = sandwich.split(Spread)
        NewSandiwch = "".join(Loafs)
        if (len(NewSandiwch) >= wordLength): 
            return flatten([Spread, unwrap(NewSandiwch, se, wordLength)])
        else: 
            return [Spread]
    else:
        return unwrap(sandwich, se, wordLength)

print(unwrap('brbacpattyonead', set(['bacon', 'patty', 'bread']), 5))
#print(unwrap('stappleyle', set(['style', 'apple']), 5))
#print(unwrap('ababaa', set(['aba', 'sen']), 5))
