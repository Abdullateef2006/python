
print("Hello world!")

myVar1 = 6
myVar2 = 8
lastVar = myVar1 + myVar2
print(lastVar)

x = 40
y = 2
print(x & y)
print(x ^ y)
print(x << y)
print(x >> y)
print(~x)
print(x > 60 & 60 > 20)

Name = "Abdullateef"
Name2 = "Jimoh"
print('l' in Name)
print('b' not in Name)
print('j' not in Name)
print(Name is Name2)
print(Name is not  Name2)

print(id(Name))
print(id(Name2))
print(Name[0])
print(len(Name))
print(Name[-1])
print(Name[-11])
print(Name[0:3])
print(Name[6:])
print(Name.count('l'))
print(Name.count('a',2,10))
print(Name.count('e'))
print(Name[4:9])
myNum = [5,7,9,4,2,0,1]
total = len(myNum)
count = 0
while count < total :
    print(myNum[count])
    count += 2
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = a + b
print(c)
num1 = int(input('Enter a number: '))
if num1 % 2 == 0:
    print(num1," is an even Number")
else :
    print(num1," is an odd Number")

message = " assalam alaikum its wednesday today "
message1 = message.lstrip()
message2 = message.rstrip()
print(message2)
print(message1)
print(message)
print(message.title())

url = "https://wwww.microsoft.com"
simpleURL = url.removeprefix('https://')
print(simpleURL)
names = ("Abdullateef","Sodiq","Habeeb","Jimoh")
print(names[0].title())
fName = "Abdullateef"
lName = " Jimoh"
fullName = f"{fName}{lName}"
print(fullName)
print(f"Assalam Alaikum, {fullName.title()}")

friend = "Sodiq"
friend_request = f"Assalam Alaikum {friend.upper()} I want to invite you to join me in python"
print(friend_request)

says_by = "Prophet Muhammad "
saying = '" Knowledge acquisition is compulsory for every muslims"'
# hadith = f"{says_by}{saying}"
print(f"{says_by} said {saying}")
print("Languages : \n\tPython\n\tJavascript\n\tCSS\n\tHtml")

myNames = ["Abdullateef","Sodiq","AbdulQudus","Jimoh"]
counter = 0
print("Names:\n")
while counter < len(myNames) :
    print("\t", myNames[counter])
    counter += 1

website = "python.com"
simpleWebsite = website.removesuffix(".com")
print(simpleWebsite)

a = 0.2
b = 0.1
c = a + b
print(c)
d = 3 * 0.1
print(d)

