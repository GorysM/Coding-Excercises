petList = []
counter=0


class Pet:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def displayInfo(self):
        print(f"The name of your pet is: {self.name} ")
        print(f"The age of your pet {self.name} is: {self.age} ")
        print(f"The weight of your pet {self.name} is {self.weight} Kgs ")
        
def petCreate (counter):
    name = input(f"Enter the name of your {counter} pet ").lower()
    age = int(input(f"Enter the age for the {counter} pet "))
    weight = float(input(f"Enter how much the {counter} pet weight's "))
    pet = Pet(name,age,weight)
    return pet

pets = int(input("Enter how many pets do you have: "))
for i in range(1,pets+1):
    counter+=1
    if counter <= 0:
        print("You need to insert a pet to proceed. ")
    else: 
        pets = petCreate(i)
        petList.append(pets)
for pets in petList:
    pets.displayInfo()

def filteredWeight(petList):
    counter=0
    for pets in petList:
        if pets.weight >=10:
            counter+=1
    if counter > 0:
            print(f"There are {counter} pets over 10Kgs")
    else:
        print("There are no pets over 10Kgs.")
def filteredNames (petList):
    counter = 0
    for pets in petList:
        if pets.name == "sissy":
            counter+=1
    if counter > 0:
            print(f"There are {counter} pets with the name Sissy")
    else:
        print("No pets found with the name Sissy")
def weightAverage(petList):
    if len(petList) > 0:
        weightAverage = sum(pet.weight for pet in petList)/len(petList)
        print(f"The weighting average of your pets is {weightAverage: .2f}  kgs.")         
    else:
        print("No pets to calculate the average weight.")
        
filteredWeight(petList)
filteredNames (petList)
weightAverage(petList)