#FIRST HALF
"""
file = open("input.txt").readlines()
valid = 0

for index, lines in enumerate(file):
    charcount = 0
    file[index] = lines.split()
    file[index][0] = file[index][0].split('-')
    file[index][1] = file[index][1].replace(':','')
    for chars in file[index][2]:
        if chars == file[index][1]:
            charcount += 1
    if charcount >= int(file[index][0][0]) and charcount <= int(file[index][0][1]):
        valid += 1
    print(file[index])

print(valid)
"""

#SECOND HALF
file = open("input.txt").readlines()
valid = 0

for index, lines in enumerate(file):
    file[index] = lines.split()
    file[index][0] = file[index][0].split('-')
    
    char = file[index][1].replace(':','')

    numone = int(file[index][0][0])-1
    numtwo = int(file[index][0][1])-1
    password = file[index][2]


    if (password[numone] == char) ^ (password[numtwo] == char):
        valid += 1
    print(file[index])

print(valid)