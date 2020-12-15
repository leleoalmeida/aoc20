import copy
bus = open('input.txt').read().splitlines()
numbrs = []
big = 0
big_id = 0

bus[1] = bus[1].split(',')


for i, id in enumerate(bus[1]):
    if id != 'x':
        bus[1][i] = int(id)
        numbrs.append(bus[1][i])
        if int(id) > big:
            big = int(id)
            big_id = i

print(numbrs)
difs = copy.deepcopy(bus[1])

# for i, id in enumerate(bus[1]):
#     difs[i] = i - big_id


# print(bus[1])
# print(difs)


# def check(bus_no):
#     x = int(bus[0])
#     while x % bus_no != 0:
#         x += 1
#     print(x, bus_no)

# for i, id in enumerate(bus[1], start=0):
#     difs[i] = i


# boolean = True


# # for id in bus[1]:
# #     if id != 'x':
# #         int_id = int(id)
# #         check(int_id)

# x = 1000716
# while boolean:
#     attempt = 0
#     check = 0
#     for i, a in enumerate(bus[1]):
#         attempt += 1
#         if a != 'x' and x+difs[i] % int(a) == 0:
#             check += 1
#         else:
#             break
#     if check == attempt:
#         boolean = False
#     else:
#         x += 937
#     print(x)
# print(x)
    
    
