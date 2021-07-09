def FlattendGroupArray(array):
    FlattenArray = [] 
    for index, group in enumerate(array):
        FlattenArray.extend(group)
    return FlattenArray

def getTop(li, n):
    top = li[0:n]
    del li[0:n] 
    return top

def getBottom(li,n):
    if len(li) >= n:
        bottom = li[len(li) - n:len(li)][::-1]
    else:
        bottom = li[0:len(li)]
    del li[len(li) - n:len(li)] 
    return bottom

def checkInner(li, n, index):
    if len(li) > 0 and index < len(li):
        if type(li[index]) is list:
            return top_and_bottom(li, n)
        else:
            return li checkInner(li, n, index + 1)
    return li

def top_and_bottom(li, n):
    top = getTop(li, n)
    checkInner(top, n, 0)
    bottom = getBottom(li,n)
    if len(li) > 0:
        return FlattendGroupArray([top, bottom, top_and_bottom(li, n)])
    else:
        if len(top) == n:
            return FlattendGroupArray([top, bottom])
        else:
            return li 

#print(top_and_bottom([], 5))
#print(top_and_bottom([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 2))
#print('>>>>')
#print([1, 2, 20, 19, 3, 4, 18, 17, 5, 6, 16, 15, 7, 8, 14, 13, 9, 10, 12, 11])

#print(top_and_bottom([1,2,3,4,5,6,7], 2))

print(top_and_bottom([1, [2, [3, 4], 5], [6, [7, [8, 9], 10]]], 1))
print('>>>>')
print([1, [6, [7, 10, [8, 9]]], [2, 5, [3, 4]]])
