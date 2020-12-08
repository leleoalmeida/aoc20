import copy
original = open('input.txt').read().splitlines()
code = open('input.txt').read().splitlines()

for i, line in enumerate(code):
    code[i] = line + ' 0'
    code[i] = code[i].split()
    
    code[i][1] = int(code[i][1])
    code[i][2] = int(code[i][2])

for i, line in enumerate(original):
    original[i] = line + ' 0'
    original[i] = original[i].split()
    
    original[i][1] = int(original[i][1])
    original[i][2] = int(original[i][2])

op = offset = line = accumulator = 0

stop = True
lines = set()

while code[line][2] != 1:
    op = code[line][0]
    offset = code[line][1]
    lines.add(line)

    code[line][2] += 1
    if op == 'nop':
        line += 1
    elif op == 'jmp':
        line += offset
    elif op == 'acc':
        line += 1
        accumulator += offset
print('First result: '+ str(accumulator))


lines = sorted(lines)
for i, y in enumerate(code):
        code[i][2] = 0

for x in lines:
    newcode = copy.deepcopy(original)

    if newcode[x][0] == 'nop':
        newcode[x][0] = 'jmp'
    elif newcode[x][0] == 'jmp':
        newcode[x][0] = 'nop'


    opx = 0
    offsetx = 0
    linex = 0
    accumulatorx = 0

    while newcode[linex][2] != 1:
        opx = newcode[linex][0]
        offsetx = newcode[linex][1]
        lastacc = accumulatorx

        newcode[linex][2] += 1

        if opx == 'nop':
            linex += 1
        elif opx == 'jmp':
            linex += offsetx
        elif opx == 'acc':
            linex += 1
            accumulatorx += offsetx
        print('Second result: ', lastacc)
