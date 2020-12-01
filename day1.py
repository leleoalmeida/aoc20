file = open("input.txt").readlines()

for i, number in enumerate(file):
    file[i] = int(number.replace('\n', ''))
    
for number in file:
    for numero in file:
        for nummer in file:
            if (number+numero+nummer) == 2020:
                print(number*numero*nummer)
                break