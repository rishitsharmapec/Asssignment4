import random
i=1
print("Hello Welcome to this Multiplication game answer the following")
while i<=10 :
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(num1,"X",num2)
    ans1 = int(input("Enter Answer"))
    if ans1 == num1 * num2:
        print("Well done,Right Answer")
    else:
        print("Sorry Wrong Answer")
    i = i + 1

