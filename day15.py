input = [9,19,1,6,0,5,4]

turn = len(input)
number = input[-1]
storage = {}
for i, v in enumerate(input):
    storage[v] = i + 1


while turn < 30000000:
    if not storage.get(number, None):
        storage[number] = turn
        number = 0
        turn += 1
    else:
        last_seen = storage[number]
        storage[number] = turn
        number = turn - last_seen
        turn += 1

print(number)



#FIRST HALF
#import copy
# numbers = [9,19,1,6,0,5,4]
# # numbers = [0,3,6]

# numlast = {
#   9: 1,
#   19: 2,
#   1: 3,
#   6: 4,
#   0: 5,
#   5: 6,
#   4: 7
# }

# numcopy = 0

# while len(numbers) < 2020:
#     last = numbers[len(numbers)-1]
#     if last not in numbers[:-1]:
#         numbers.append(0)
#         numcopy = numlast.copy()
#         numlast[0] = len(numbers)
#     else:

#         i = len(numbers) - numcopy[last]
#         numcopy = numlast.copy()
#         numbers.append(i)
#         numlast[i] = len(numbers)

        

# print(numbers[30000000-1])
