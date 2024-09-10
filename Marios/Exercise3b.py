class Pet: 
    def __init__(self, name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def display (self):
        counter=0
        print(f"The name of your {counter+1} pet is: {self.name}")
        print(f"The age for your {counter+1} pet is: {self.age}")
        print(f"The weight for your {counter+1} pet is: {self.weight}")

def petCreate (counter):
        name = input(f"Tell me the name for your {counter} pet: ").lower()
        age = int(input(f"Insert the age for the {counter} pet: "))
        weight = float(input(f"Enter the weight for the {counter} pet: "))
        pets = Pet(name, age, weight)
        return pets 
petList = []
counter = 0
pets = int(input("Please insert the number of your pets you want to insert: "))
for i in range(1, pets+1):
    counter+=1
    if counter < 0:
        print("You need to enter how many pets you have otherwise we cannot proceed. Try again. ")
    else: 
        pets = petCreate(i)
        petList.append(pets)
for pets in petList:
    pets.display()

def filterWeight(petList):
    counter= 0
    for pets in (petList):
        if pets.weight >= 10:
            counter+=1
    if counter >0:
            print(f"There are {counter} pets weighted over 10Kgs")
    else:
        print("There are not any pets weighted over 10Kgs.") 
def filterName (petList):
    counter=0
    for pets in (petList):
        if pets.name =="sissy":
            counter+=1
    if counter >0:
        print(f"There are {counter} pets with the name sissy.")
    else: 
        print("No pets found named sissy.")
def weightAverage(petList):
    if len(petList) > 0:
        weightAverage = sum(pet.weight for pet in petList)/len(petList)
        print(f"The weighting average of your pets is {weightAverage: .2f}  kgs.")         
    else:
        print("No pets to calculate the average weight.")
        
filterWeight(petList)
filterName (petList)
weightAverage(petList)