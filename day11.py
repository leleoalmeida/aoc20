import copy
import numpy as np

seats = open('input.txt').read().splitlines()

def split_str(chars):
  return [ch for ch in chars]

for i, x in enumerate(seats):
    seats[i] = split_str(x)

seats = np.pad(seats, pad_width=1, mode='constant')  
tempseats = copy.deepcopy(seats)


def check(x, y):
    count = 0

    if seats[x-1][y-1] == '#':
        count += 1
    if seats[x-1][y] == '#':
        count += 1
    if seats[x-1][y+1] == '#':
        count += 1
    if seats[x][y-1] == '#':
        count += 1
    if seats[x][y+1] == '#':
        count += 1
    if seats[x+1][y-1] == '#':
        count += 1
    if seats[x+1][y] == '#':
        count += 1
    if seats[x+1][y+1] == '#':
        count += 1
    if seats[x][y] == 'L' and count == 0:
        tempseats[x][y] = '#'
    if seats[x][y] == '#' and count >= 4:
        tempseats[x][y] = 'L'


def diagonal(x, y):
    m = x
    n = y
    boolean = True
    count = 0

    #up left
    while m > 0 and n > 0 and boolean:
        m -= 1
        n -= 1
        if seats[m][n] == '#' or seats[m][n] == 'L':
            boolean = False
            if seats[m][n] == '#':
                count +=1
    m = x
    n = y
    boolean = True    
    #up
    while m > 0 and boolean:
        m -= 1
        if seats[m][n] == '#' or seats[m][n] == 'L':
            boolean = False
            if seats[m][n] == '#':
                count +=1
    m = x
    n = y
    boolean = True
    #up right
    while m > 0 and n < len(seats[x])-1 and boolean:
        m -= 1
        n += 1
        if seats[m][n] == '#' or seats[m][n] == 'L':
            boolean = False
            if seats[m][n] == '#':
                count +=1    
    m = x
    n = y
    boolean = True
    #left
    while n > 0 and boolean:
        n -= 1
        if seats[m][n] == '#' or seats[m][n] == 'L':
            boolean = False
            if seats[m][n] == '#':
                count +=1             
    m = x
    n = y
    boolean = True
    #right
    while n < len(seats[x])-1 and boolean:
        n += 1
        if seats[m][n] == '#' or seats[m][n] == 'L':
            boolean = False
            if seats[m][n] == '#':
                count +=1  

    m = x
    n = y
    boolean = True
    #down left
    while m < len(seats)-1 and n > 0 and boolean:
        m += 1
        n -= 1
        if seats[m][n] == '#' or seats[m][n] == 'L':
            boolean = False
            if seats[m][n] == '#':
                count +=1 

    m = x
    n = y
    boolean = True
    #down
    while m < len(seats)-1 and boolean:
        m += 1
        if seats[m][n] == '#' or seats[m][n] == 'L':
            boolean = False
            if seats[m][n] == '#':
                count +=1 

    m = x
    n = y
    boolean = True

    #down right
    while m < len(seats)-1 and n < len(seats[x])-1 and boolean:
        m += 1
        n += 1
        if seats[m][n] == '#' or seats[m][n] == 'L':
            boolean = False
            if seats[m][n] == '#':
                count +=1
    
    if seats[x][y] == 'L' and count == 0:

        tempseats[x][y] = '#'
    if seats[x][y] == '#' and count >= 5:
        tempseats[x][y] = 'L'    


boolean = True

while boolean:
    seats = copy.deepcopy(tempseats)
    for i, a in enumerate(seats):
        for j, b in enumerate(a):
            
            if (i != 0 and i != len(seats)) and (j != 0 and j != len(a)):
                diagonal(i, j)
    if (seats==tempseats).all():
        boolean = False

occ = 0

for a in seats:
    for b in a:
        occ += b.count('#')

print(occ)