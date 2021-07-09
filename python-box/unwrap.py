def flatten(NestedArray):
    if NestedArray == []:
        return NestedArray
    if isinstance(NestedArray[0], list):
        return flatten(NestedArray[0]) + flatten(NestedArray[1:])
    return NestedArray[:1] + flatten(NestedArray[1:])

def findSpread(index, wordLength, se, sandwich):
    endStart = len(sandwich) - (wordLength - index)
    word = sandwich[0:index] + sandwich[endStart :len(sandwich)]
    if word in se: 
        return [word, sandwich[index:endStart]]
    else:
        return findSpread(index + 1, wordLength, se, sandwich)

def unwrap(sandwich, se, wordLength):
    se = list(se)
    word = findSpread(1, wordLength, se, sandwich)
    if (word[1]):
        return flatten([unwrap(word[1], set(se), wordLength), word[0]])
    else:
        return word[0]


print(unwrap('brebacpattyonad', set(['bacon', 'patty', 'bread']), 5))
#print(unwrap('ababaa', set(['aba', 'sen']), 3))
