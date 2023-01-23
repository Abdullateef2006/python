score = int(input("Enter your Score: "))
if score >= 80:
    print("You got an A ")
elif score >= 70:
    print("You got a B")
elif score >= 60:
    print("You got a C")
elif score >= 50:
    print("You got a D")
elif  score >= 40:
    print("You got an E")
elif score < 40:
    print("You got a F")
else:
    print("You have to enter your correct score")
