friends = int(input("Enter how many friends do you have: "))
ageList = []
nameList = []

def ageFilteredList (ageList):
    if 40 in ageList:
        ageCounter = ageList.count(40)
        print(f"There are {ageCounter} of your friends that are 40 years old.")
    else: 
        print("No age 40 matches found")
        
def filteredNameList (nameList):
    nameCounter = nameList.count('marios')
    if 'marios' in nameList:       
        print(f"There are {nameCounter} named marios")
    else: 
        print("No marios matches found")
        
for i in range (friends):
    age = int(input(f"Enter your friend's {i + 1} age: "))
    ageList.append(age)
    name = input(f"Enter your {i + 1} friends name: ")
    nameList.append(name)

ageFilteredList(ageList)
filteredNameList(nameList)