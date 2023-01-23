cars = ["sienna","corrolla","venza","lexus","camry"]
car = cars[-5]
print(car)
statement = "my first car is "
print(f"{statement}{cars[2]}")
message3 = f"{statement}{cars[2]}"
print(message3)
message4 = f"My first car is {cars[2].title()}"
print(message4)

carsRename = cars[2] = "bentley"
print(cars)

i = 0
while i < len(cars):
    print(cars[i].title())
    i += 1

cars.append("Honda")
print(cars)
cars.insert(2, "Land Rover")
print(cars)
del cars[3]
print(cars)
cars.pop()
print(cars)
lastRemoved = cars.pop(2)
print(lastRemoved)
cars.remove("corrolla")
print(cars)

nameList = []
nameExtend = ["Abdullateef","Sodiq","Habeeb","Latifat","Aishat","Latifat","Jimoh","AbdulQudus","AbdulRahmon","Faruk"]
# nameList = nameExtend[:]
nameList.extend(nameExtend)
nameList[2] = "AbdulRazak"
nameList[8] = "Abdulmuhmin"
nameList.insert(0, "AbdulMalik")
nameList.insert(4, "AbdulSalam")
nameList.append("Sultan")
print(nameList)
nameList.pop()
del nameList[4]
nameList.remove("Aishat")
print(nameList)

print("Names: ")
for name in nameList:
    print("\t",f"{name} is one of the members")

nameList.sort()
print(nameList)
nameList.sort(reverse=True)
print(nameList)

for i in range(2,11,2):
    print(i)

squares = []
for i in range(1,11):
    i = i**2
    squares.append(i)
    print(i)
print(squares)

print(max(squares))
print(min(squares))
print(sum(squares))

square = [i**2 for i in range(1, 11)]
print(square)

list1 = []
for i in range(1,21,2):
    list1.append(i)
print(list1)

list2 = []
for i in range(3,31):
    list2.append(i)
print(list2)

list3 = []
for i in range(1,11):
    i **= 3
    list3.append(i)
print(list3)

list4 = [i**3 for i in range(1,11)]
print(list4)
print(list4[3:7])
print(list4)
print(nameList[4:8])
# for name in nameList[:6]:
#     print(name.title())

# for names in nameList[4:]:
#     print(names.title())

for name in nameList:
    if name == 'Sodiq':
        print(name.upper())
    else:
        print(name.lower())
secret = [100,101,101,122,32,110,117,116,115]
for i in secret:
    print(chr(i))