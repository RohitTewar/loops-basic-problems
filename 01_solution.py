#check total how many positive numbers in the list
#using for loop and if loop

numbers = [1, 2,3 ,4 , -5, -6, -7, -8, -9, 11, 12, 13 ]
positive_numbers_count = 0

for num in numbers:
    if num>0:
        positive_numbers_count += 1
print("total positive numbers is :", positive_numbers_count)
