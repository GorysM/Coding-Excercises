friends = int(input("Tell me how many friends do you have: "))
nameList = []
ageList = []
counter=0
for i in range (friends):
    counter+=1
    names = input(f"Tell me the name of your {counter} friend(s): ").lower()
    nameList.append(names)
    ages = int(input(f"Tell me the age of your {counter} friend(s): "))
    ageList.append(ages)
def filteredNames(nameList):
    counter1 = 0
    for names in nameList:
        if names == "marios":
            counter1 += 1
    if counter>0:
        print(f"There are {counter1} of your friends names Marios: ")
    else:
        print("There are none of your friends named Marios.")

def filteredAges(ageList):
    counter2 = 0
    for age in ageList:
        if 40 <= age <= 60:
            counter2 += 1
    if counter2 > 0:
        print(f"There are {counter2} friends in the range of 40 to 60 years old. ")
    else:
        print("There are none of your friends within the range of 40 and 60 yearls old.")
        
filteredAges(ageList)
filteredNames(nameList)