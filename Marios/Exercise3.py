class Pet:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def display (self):
        print(f"The name of your pet is {self.name}")
        print(f"The age of your pet is {self.age}")
        print(f"The weight of your pet is {self.weight} kg")

def petCreate(counter):
    name = input(f"Enter the name of your {counter} pet: ").lower()
    age = int(input(f"Enter the age of your {counter} pet: "))
    weight = float(input(f"Enter the weight of your {counter} pet in Kg: "))
    pets = Pet(name, age, weight)
    return pets

def filteredPets(petList):
    nameCounter = 0
    for pet in petList: 
        if pet.name == "sissy":  
            nameCounter += 1
    if nameCounter > 0:
        print(f"There are {nameCounter} pets named Sissy.")
    else:
        print("None of the pets are named Sissy.")
def weightCounter(petList):
    weightCounter = 0
    for pet in petList:
        if pet.weight >= 10:  
            weightCounter += 1
    if weightCounter > 0:
        print(f"There are {weightCounter} pets that are above 10kgs.")
    else:
        print("There are no pets over 10kgs.") 
        
def weightAverage(petList):
    if len(petList) > 0:
        weightAverage = sum(pet.weight for pet in petList)/len(petList)
        print(f"The weighting average of your pets is {weightAverage: .2f}  kgs.")         
    else:
        print("No pets to calculate the average weight.")
        
numberOfPets = int(input("How many pets do you have?"))
counter = 0
petList = []

for i in range(1,numberOfPets+1):
    counter+=1
    if counter <= 0:
        print("You need to insert a number of pets to proceed, try again.")
    else: 
        pet = petCreate(i)
        petList.append(pet)
for pet in petList:
    pet.display()
    
filteredPets(petList)
weightCounter(petList)
weightAverage(petList)
