slope = open("input.txt").readlines()
#finding the width of the slope based on the first line's length
width = len(slope[0].replace('\n',''))
'''
trees = 0


i = 0

for x in slope:
    print(i, x[i])

    if x[i] == '#':
        trees += 1
    if (i + 3) > width-1:
        i += 3-width
    else:
        i += 3

print(trees)
'''

trees = [0, 0, 0, 0, 0]
shift = [1, 3, 5, 7, 1]
index = [1, 1, 1, 1, 2]

total = 0

for k, t in enumerate(trees):
    
    i = 0   
    for j, x in enumerate(slope):
        if j % index[k] == 0:    
            if slope[j][i] == '#':
                trees[k] += 1
            if (i + shift[k]) > width-1:
                i += shift[k]-width
            else:
                i += shift[k]
            j += index[k]
    print(trees[k])

total = trees[0]*trees[1]*trees[2]*trees[3]*trees[4]
print(total)
