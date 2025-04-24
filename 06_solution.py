# compute factorial of a number using while loop
#Factorial calculator

number = int(input("select a number :"))
factorial =1

while number >0:

   # factorial = factorial * number
   # number = number -1

    factorial *= number
    number-= 1
print("factorial:", factorial)

# two ways i show to slove a problem use line no. 9 and 10 or use 12 and 13 to compute the solution