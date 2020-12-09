numbers = open('input.txt').read().splitlines()
numbers = [int(i) for i in numbers]

# print(numbers)
global begin
begin = 0
sums = set()
preamble = numbers[:begin+25]
global count
count = 0


def check():
    begin = 0
    for i, x in enumerate(numbers, start=25):
        preamble = numbers[:begin+25]

        sums.clear()
        count = 0   
        for i, x in enumerate(preamble, start=1):
            for y in preamble[i:]:
                temp = x+y
                count += 1
                sums.add(temp)
        if numbers[i] not in sums:
            return numbers[i]
        begin +=1

def contiguous(fail):
    
    for j, x in enumerate(numbers):
        start = j
        rangex = []
        sumall = 0
        while sumall < fail:
            rangex.append(numbers[start])
            sumall += numbers[start]
            start += 1
        rangex.sort()
        if sumall == fail:
            print('Sum is', rangex[0] + rangex[len(rangex)-1])
            break
    print('done')


contiguous(check())