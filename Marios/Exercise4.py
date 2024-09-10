shirts = int(input("Insert how many shirts do you have? "))
counter=0
shirtsDict = {}
class Shirt: 
    def __init__(self, brand,made,price):
        self.brand = brand
        self.made = made
        self.price = price
def shirtCreate(counter):
    brand = input(f"Insert the brand for the {counter} shirt: ").lower()
    made = input(f"Insert where the {counter} shirt was made: ").lower()
    price = float(input(f"Insert the price for the {counter} shirt: "))
    shirts = Shirt(brand,made,price)
    return shirts
    
for i in range (1, shirts+1):
    counter+=1
    if counter <=0:
        print("You need to insert shirts to proceed. Try again! ")
    else:
        shirts = shirtCreate(i)
        shirtsDict[counter] = shirts
counterChina = 0        
for shirts in shirtsDict.values():
    if shirts.made == "china":
        counterChina+=1
if counterChina <= 0 :
    print (f"No shirts found been made in China!")
else:
    print(f"There are {counterChina} shirts been made in China!")
def filterPrice(shirtsDict,counter):
    for shirts in shirtsDict.values():
        if shirts.price <= 100:
            counter+1
    if counter <=0 :
        print("No shirt found costs over £100!")
    else: 
        print(f"There are {counter} shirts found costs £100 and over!")
def priceAverage(shirtsDict):
    if len(shirtsDict) > 0:
        price_average = sum(shirt.price for shirt in shirtsDict.values()) / len(shirtsDict)
        print(f"The price average of your shirts is £{price_average:.2f}.")
    else:
        print("No prices found to calculate the average.")
filterPrice(shirtsDict,counter)
priceAverage(shirtsDict)