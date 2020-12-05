scan = open('input.txt').readlines()
highest = 0

#SECOND HALF
plane = [0] * 1024
for index, x in enumerate(plane):
    plane[index] = index


for i, passes in enumerate(scan):
    row = [0] * 128
    seat = [0] * 8
    scan[i] = passes.replace('\n','')
    for x in range(128):
        row[x] = x

    for x in range(8):
        seat[x] = x

    for char in passes:
        length = int(len(row)/2)
        slength = int(len(seat)/2)

        if char == 'F':
            row = row[:length] 
        elif char == 'B':
            row = row[length:]
        elif char == 'L':
            seat = seat[:slength] 
        elif char == 'R':
            seat = seat[slength:]
    endrow = row[0]
    endseat = seat[0]
    seatid = endrow*8+endseat
    plane[seatid] = 'x'

for i, seat in enumerate(plane):
    if seat != 'x' and (plane[i-1] == 'x' and plane[i+1] == 'x'):
        print('Your seat:',seat)


#FIRST HALF
'''
for i, passes in enumerate(scan):
    row = [0] * 128
    seat = [0] * 8
    scan[i] = passes.replace('\n','')
    for x in range(0, 127):
        row[x] = x

    for x in range(0, 7):
        seat[x] = x

    for char in passes:
        length = int(len(row)/2)
        slength = int(len(seat)/2)
        if char == 'F':
            row = row[:length] 
        elif char == 'B':
            row = row[length:]
        elif char == 'L':
            seat = seat[:slength] 
        elif char == 'R':
            seat = seat[slength:]
    endrow = row[0]
    endseat = seat[0]
    if (endrow * 8 + endseat) > highest:
        highest = (endrow * 8 + endseat)
         
    print(highest)'''