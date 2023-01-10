year= int(input("Enter an Year "))
if year%100!=0 and year%4==0 :
    print("Year is a Leap Year")
elif year%100==0 and year%400==0:
    print("Year is a Leap Year")
else:
    print("Year is not a Leap Year")
