marks = int(input("Enter your marks: "))
if marks > 500 or marks < 0:
    print("Invalid marks")
elif marks>=400 and marks<=500:
    print("You got an A grade")
elif marks>=300 and marks<400:
    print("You got a B grade")
elif marks>=200 and marks<300:
    print("You got a C grade")
elif marks>=100 and marks<200:
    print("You got a D grade")
else:
    print("You got an F grade")