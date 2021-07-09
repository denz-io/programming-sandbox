ListRange = int(input())
line = input()
IDList = line.split()
for index in range (0, ListRange):
    IDList[index] = int(IDList[index])
    
X = IDList[0]
Y = IDList[1]

Z = ((X & Y) ^ (X ^ Y) | (X ^ Y))
MaxValue = Z
X = Y 

for index in range(2, ListRange):
    Y = IDList[index]
    Z = ((X & Y) ^ (X ^ Y) | (X ^ Y))
    if MaxValue < Z:
        MaxValue = Z
    X = Y

print(MaxValue)
