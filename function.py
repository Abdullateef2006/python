def greeting():
    print("AsSalam Alaikum")
greeting()

def greetings(name):
    print(f"AsSalam Alaykum {name}")
greetings("Abdullateef")

carsNames = ["sienna","corrolla","venza","lexus","camry"]
def cars(cartype, carName):
     for x in carsNames:
        print(f"car {cartype} has a model called {x}")
cars("Toyota", carsNames )

carsType = {
    "Toyota" : "Sienna",
    "Benz" : "4matic",
    "Honda" : "Accord"
}
def carModel(value):
    for x,y in carsType.items():
        print(f"car {x} has a model called {y}")
carModel(carsType)


shortMessages = ["Hi","AsSalam Alaikum","Wa Alaykum Salam","How are you doing"]

def message():
    print(shortMessages)

def sendMessages():
    newMessages = []
    while shortMessages:
        storedMessages = shortMessages.pop(0)
        newMessages.append(storedMessages)
    print(newMessages)



message()
sendMessages()
    


