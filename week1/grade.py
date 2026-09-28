score= int(input("Enter the candidate score: "))

if 90 <=score <=100:
    print("Grade: A")
elif 80<=score <90:
    print("Grade: B")
elif score>=70 and score<80:
    print("Grade: C")
elif score>=60 and score<70:
    print("Grade: D")
else:
    print("\033[31m" + "Grade: F" "\033[0m")
    
    