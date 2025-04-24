# find the first non repeated character

input_str= "i love biryani"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("char is :", char)
       # break
