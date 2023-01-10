marks=float(input("Enter marks of the student "))
if marks<25 and marks>=0 :
    print("Grade is F")
elif 25<=marks and marks<45 :
    print("Grade is E")
elif 45<=marks and marks<50 :
    print("Grade is D")
elif 50<=marks and marks<60 :
    print("Grade is C ")
elif 60<=marks and marks<=80 :
    print("Grade is B")

elif marks>80 and marks<=100:
    print("Grade is A")
else :
    print("Marks are not in the range from 0 to 100")
