ageList = []
nameList= []
counter = 0

friends = int(input("Enter a number for how many do you have: "))
for i in range(friends):
    counter+=1
    names = input(f"Enter the name of your {counter} friend: ").lower()
    nameList.append(names)
    ages = int(input(f"Enter the age of your {counter} friend: "))
    ageList.append(ages)
def filteredNames(nameList):
    nameCounter = nameList.count("marios")
    if nameCounter > 0:
        print(f"There are {nameCounter} friend(s) with the name Marios.")
    else:
        print("There aren't any of your friends named Marios.")
def filteredAges (ageList):
    ageCounter = 0
    for age in ageList:
        if 40 <= age <= 60:
            ageCounter+=1
    if ageCounter > 0:
        print (f"You have {ageCounter} friend(s) between the age 40 and 60.")
    else: 
        print("There are not any of your friends between the age 40 and 60.")

filteredNames(nameList)
filteredAges(ageList)