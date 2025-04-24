#valid input from user 

while True:
    number = int(input("enter the vaild input b/w 1 to 100:"))
    if 1<= number <=100:
        print("vaild input thanks")
        break
    else:
        print("invalid number")