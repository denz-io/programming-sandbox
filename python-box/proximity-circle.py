MyScore = 14
BarkadaSize = 6   
NumberOfFriends = 10  
Friends = [
    { "Name": "NICOLE", "Score": 30},
    { "Name": "LAUREN", "Score": 6},
    { "Name": "MILA", "Score": 24},
    { "Name": "CHARLOTTE", "Score": 12},
    { "Name": "KIAN", "Score": 15},
    { "Name": "SAMUEL", "Score": 1},
    { "Name": "AMBER", "Score": 8},
    { "Name": "NIAMH", "Score": 16},
    { "Name": "MAYA", "Score": 23},
    { "Name": "HOLLY", "Score": 8},
]
Barkada = []

def OrderLexecographical(ToSort):
    return sorted(ToSort, key = lambda x: x["Name"][::-1], reverse = True)

def GroupArrayByElement(element, array):
    SortBy = []
    SortCounter = 0
    for index, friend in enumerate(array):
        if len(SortBy) == 0:
            SortBy.append([friend])
        else:
            if (friend[element] == SortBy[SortCounter][0][element]):
                SortBy[SortCounter].append(friend)
            else:
                SortCounter += 1 
                SortBy.append([friend])
    return SortBy

def FlattendGroupArray(array):
    FlattenArray = [] 
    for index, group in enumerate(array):
        FlattenArray.extend(group)
    return FlattenArray

def DoSortByScoreOrName(SortedArray):
    for index, group in enumerate(SortedArray):
        if len(group) > 1:
            if group[0]['Score'] == group[1]['Score']:
                if len(group[0]['Name']) == len(group[1]['Name']):
                    SortedArray[index] = OrderLexecographical(group)
                else:
                    SortedArray[index] = sorted(group, key=lambda x: len(x["Name"]))
    return SortedArray;

def DoGroupSortByProximity(SortedArray):
    for index, group in enumerate(SortedArray):
        if len(group) > 1:
            if group[0]['Proximity'] == group[1]['Proximity']:
                    SortedArray[index] = sorted(group, key=lambda x: x["Score"])
    return SortedArray;

for index, friends in enumerate(Friends):
    Friends[index]["Proximity"] = abs(MyScore - friends["Score"])

SortedArray = FlattendGroupArray(
    DoGroupSortByProximity(
    GroupArrayByElement('Proximity', 
    sorted(FlattendGroupArray(
    DoSortByScoreOrName(
    GroupArrayByElement('Score', 
    sorted(Friends, key=lambda x: x["Score"])))), key=lambda x: x["Proximity"]))))

for index in range(0, BarkadaSize):
    print(SortedArray[index]["Name"])

if (NumberOfFriends != BarkadaSize):
    BPlus1 = SortedArray[BarkadaSize]
    for index, friends in enumerate(SortedArray):
        if abs(BPlus1["Score"] - friends["Score"]) == SortedArray[0]["Proximity"]:
            if index < BarkadaSize:
                print(BPlus1["Name"])
            else:
                print(str(BPlus1["Name"]) + ", " + str(friends["Name"]))
            break
        elif index == len(SortedArray) - 1:
            print(str(BPlus1["Name"]) + ", almost")
            break
