dictionary = {
    "Name": "Abdullateef",
    "lName": "Jimoh",
    "Age": 16
}
dictionary["school"] = "Saint Saviors High School"
dictionary["Age"] = 17
print(dictionary)
# dictionary.pop("school")
del dictionary["school"]
print(dictionary)

subjects = {
    "Abdullateef": "Mathematics",
    "Sodiq": "Government",
    "Aishat": "Chemistry",
    "Habeeb": "Further Mathematics",
    "AbdulQudus": "English"
}

for x, y in subjects.items():
    print(f"{x} : {y}")
print(f"Abdullateef favourite subject is {subjects['Abdullateef']}")
person_Value = subjects.get('person', 'No person value assigned')
# print(f"This person favourite subject is {subjects['person']}")
print(person_Value)


person = {
    "Name": "Abdullateef",
    "lName": "Jimoh",
    "Age": 16,
    "City": "Alimosho"
}


print("These are the person's identity \n")
print("\n", person["Name"], "\n", person["lName"],
      "\n", person["Age"], "\n", person["City"])

programmingLang = {
    "Abdullateef": ["Python", "Javascipt", "HTML"],
    "Sodiq": ["Javascript", "C", "C++"],
    "Habeeb": ["Java", "Ruby", "Rust"],
    "Aishat": ["Swift", "c#", "Lua"],
    "Latifat": ["Golang", "php", "Python"]
}

for name, lang in programmingLang.items():
    print(f"The names of the programming languages that {name} likes are")
    for myLang in lang:
        print(f"\n, {myLang}")

javaScript = {
    "concat": "Join several arrays into one",
    "lastIndexOf": "Give the last position at which a given element appears in an array",
    "pop": "Remove the last element of an array",
    "push": "Add a new element at the end",
    "reverse": "Sort elements in descending order",
    "shift": "Remove the first element of an array",
    "slice": "Pull a copy of a portion of an array into a new array",
    "splice": "Add positions and elements in a specified way",
    "toString": "Convert elements to strings",
    "unshift": "Add a new element to the beginning",
}

for x, y in javaScript.items():
    print(f"{x} : {y}")

cars_List = []
for carsNumbers in range(30):
    newCar = {
        "Name": "Camry",
        "Colour": "Red",
        "Year": 2016
    }
    cars_List.append(newCar)
for cars in cars_List[:5]:
    if cars["Colour"] == "Red":
        cars["Colour"] = "Green"
    elif cars["Colour"] == "Green":
        cars["Colour"] = "Blue"
    if cars["Year"] == 2016:
        cars["Year"] = 2013
for car in cars_List[:10]:
    print(car)

print("--------")
print("The total amount of cars we have for now is", len(cars_List))

menu = {
    "Ice Cream": "Floffy",
    "Decoration": ["Brownie", "Strawberry", "Flacks"]
}

print(f"{menu['Ice Cream']} is with the follwing decorations")
for decor in menu['Decoration']:
    print("\t", decor)

users = {
    "aJimoh": {
        "fName": "Abdullateef",
        "lName": "Jimoh",
        "email": "AbdullateefOjugbele@gmail.com",
        "Password": "Ojugbele2000"
    },
    "sJimoh": {
        "fName": "Sodiq",
        "lName": "Jimoh",
        "email": "SodiqTele@gmail.com",
        "Password": "SodiqTele50"
    },
    "latiaftJimoh": {
        "fName": "Latifat",
        "lName": "Jimoh",
        "email": "LateefatOjugbele@gmail.com",
        "Password": "LatifatJimoh"
    },
    "hJimoh": {
        "fName": "Habeeb",
        "lName": "Jimoh",
        "email": "HabeebOjugbele@gmail.com",
        "Password": "OjugbeleHabeeb"
    },
    "sJimoh": {
        "fName": "Sekinat",
        "lName": "Jimoh",
        "email": "SekinatOjugbele@gmail.com",
        "Password": "Sekinat"
    }
}


for user, userInfo in users.items():
    print(f"The info of {user} is")
    for key, value in userInfo.items():
        print(f"\t {key} : {value}")

people = {
    "southAmerican": ["America", "Mexico", "Canada"],
    "Asia": ["China", "Japan", "India"],
    "Africa": ["Nigeria", "Ghana", "Egypt"]
}

for key, value in people.items():
    print(f"The countries in {key} are")
    for x in value:
        print("\t", x)

cars = {
    "vehicle One": {
        "type": "lorry",
        "owner": "Abdullateef"
    },
    "vehicle Two": {
        "type": "Truck",
        "owner": "Sodiq"
    },
    "vehicle Three": {
        "type": "Bus",
        "owner": "Habeeb"
    },
    "vehicle Four": {
        "type": "car",
        "owner": "Latifat"
    }
}

for car, info in cars.items():
    print(f"These are the imformation of {car} :")
    for key, value in info.items():
        print(f"\t {key} : {value}")


favouritePlaces = {
    "Abdullateef": ["Lagos", "Abuja", "Oyo"],
    "Sodiq": ["Kaduna", "Jos", "Kano"],
    "Latifat": ["Akwa-Ibom", "Bayelsa", "Port-harcout"]
}

for name, place in favouritePlaces.items():
    print(f"{name} favourite places are")
    for i in place:
        print(f"\t", i)


# prompt = "\n Tell me something and i will repeat it back to you"
# prompt += "\n Enter 'Quit' to end the program: "
active = True
# while active:
#     message = input(prompt)
#     if message == 'Quit':
#         active = False
#     else :
#         print(message)
# message = ""
# while message != 'Quit':
#     message = input(prompt)
#     if message != 'Quit':
#         print(message)

order = "\n Enter the type of decoration you want on your ice cream"
order += "\n Click 'Quit' when you are done selecting: "
# while active:
#     menu = input(order)
#     if menu == 'Quit':
#         active = False
#     else :
#         print("The type of decoration you want is", menu.title())

# rules = "\n Enter you age in order to know your respective prices \n Note: 'It is free for children below 10 years': "
# while active:
#     age = int(input(rules))
#     if age < 10 :
#         print("It is free for children below 10 yrs old")
#     elif age < 18:
#         print("Your fee is 200 naira")
#     elif age < 30:
#         print("Your fee is 500 naira")
#     elif age > 30:
#         print("Your fee is 1000 naira")
#     else :
#         print("Ages can only be entered in 'figures' and not 'words'")


# num = int(input("Enter the number you want to start with: "))
# stop = int(input("Enter where you want it to stop: "))
# while num < 10:
#     num = num + 1
#     print( num)
#     if num == stop:
#         break

# num = int(input("Enter the number you want to start with: "))
# pause = int(input("Enter where you want it to pause: "))
# while num < 10:
#     num = num + 1
#     if num == pause:
#         continue
#     elif pause > 10:
#         break
#     print(num)

name = ["Abdullateef", "Sodiq", "Habeeb", "Jimoh", "Yunus"]
name1 = []

while name:
    reversed(name)
    name2 = name.pop(0)
    print(name2)
    name1.append(name2)

print(name1)
for x in name1:
    print(x)

# cars = ["Bentley","Ford","Toyota","Camry","Venza","Toyota","Lexus","Toyota","Sienna","Toyota"]
# while "Toyota" in cars:
#     cars.remove("Toyota")
# print(cars)

# responses = {

# }
# active = True
# while active:
#     name = input(" Please can you enter your name: ")
#     response = input("Who are you going to vote for ?: ")
#     responses[name] = response
#     repeat = input("Do you want to add another response (Yes/No) ")
#     if repeat == 'No':
#         active = False
#     else :
#         active = True
# print("\n ----- These are the responses of vote -----")
# for name,response in responses.items():
#     print(f"{name} would like to vote for {response}")
#     print(responses)


# responses = {
#     "Abdullateef": "",
#     "Sodiq" : "",
#     "Habeeb" : "",
#     "Aishat" : "",
#     "Latifat" : "",

# }
# active = True
# while active:

#     responses["Abdullateef"] = "Tinubu"
#     responses["Sodiq"] = "Atiku"
#     responses["Habeeb"] = "Tinubu"
#     responses["Aishat"] = "atiku"
#     responses["Latifat"] = "Tinubu"
#     repeat = input("Do you want to continue (Yes/No): ")
#     if repeat == 'No':
#         active = False


# print("\n ----- These are the responses of vote -----")
# for name,response in responses.items():
#     print(f"{name} would like to vote for {response}")
    # print(responses)


# prompts = "\n please Enter the name of your favourite Country"
# prompts += "\n (Enter 'Quit' when you are finished): "
# while active:
#     city = input(prompts)
#     if city == 'Quit':
#         continue
#     else :
#         print("I will love to go to", city.title())

# currentNumber = 0
# while currentNumber < 10:
#     currentNumber += 1
#     if currentNumber % 2 == 0:
#         continue
#     print(currentNumber)

# javascript = {}
# active = True
# while active:
#     method = input("Please can you tell me a javascript method: ")
#     meaning = input("Please can you tell me the meaning of that method: ")
#     javascript[method] = meaning
#     question = input("Please you know another javascript method: ")
#     if question == 'No':
#         active = False
# print("\n ----- These are the meaning of the methods -----")
# for x, y in javascript.items():
#     print(f"The meaning of {x} is that {y}")
