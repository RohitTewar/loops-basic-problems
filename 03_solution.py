# multiplication table printer
#skip the 4 iteration from the table

number = 4

for i in range(1,11):
    if i == 4:
        continue
    print(number, 'x', i,'=', number*i)