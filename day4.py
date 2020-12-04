passports = open("input.txt").read()
passports = passports.split('\n\n')
valid = 0

for i, x in enumerate(passports):
    passports[i] = x.replace('\n',' ')
    passports[i] = passports[i].split(' ')

    #SECOND HALF
    for j, y in enumerate(passports[i]):
        passports[i][j] = y.split(':')

for x in passports:
    
    check = 0
    if len(x) >= 7:
        for y in x:
            if y[0] == 'byr' and int(y[1])>=1920 and int(y[1])<=2002:
                check += 1
            elif y[0] == 'iyr' and int(y[1])>=2010 and int(y[1])<=2020:
                check += 1
            elif y[0] == 'eyr' and int(y[1])>=2020 and int(y[1])<=2030:
                check += 1
            elif y[0] == 'hgt':
                if 'in' in y[1]:
                    y[1] = y[1].replace('in','')
                    if int(y[1])>=59 and int(y[1])<=76:
                        check += 1            
                else:
                    y[1] = y[1].replace('cm','')
                    if int(y[1])>=150 and int(y[1])<=193:
                        check += 1 
            elif y[0] == 'hcl':
                if y[1][0] == '#':
                    
                    checktwo = 0
                    for z in y[1][1:]:
                        if z in "01234567890abcdef":
                            checktwo += 1
                            if checktwo == 6:
                                check+=1
            elif y[0] == 'ecl' and (y[1] == 'amb' or y[1] == 'blu' or y[1] == 'brn' or y[1] == 'gry' or y[1] == 'grn' or y[1] == 'hzl' or y[1] == 'oth'):
                check += 1
            elif y[0] == 'pid' and len(y[1]) == 9:
                check += 1
            print(check)
            if check == 7:
                valid +=1


#FIRST HALF
'''
for x in passports:
    check = 0
    
    if len(x) == 8:
        #checking whether all fields are valid, just in case...
        for y in x:
            if 'byr' in y or 'iyr' in y or 'eyr' in y or 'hgt' in y or 'hcl' in y or 'ecl' in y or 'pid' in y or 'cid' in y:
                check += 1
                if check >= 7:
                    valid+= 1
                    break
            else:
                break

    elif len(x) == 7:
        for y in x:
            if 'byr' in y or 'iyr' in y or 'eyr' in y or 'hgt' in y or 'hcl' in y or 'ecl' in y or 'pid' in y:
                check += 1
                if check == 7:
                    valid+= 1
                    break
            else:
                break'''

                
print(valid)
# %%
