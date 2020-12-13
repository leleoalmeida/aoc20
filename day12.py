nav = open('input.txt').read().splitlines()

print(nav)
directions = ['N', 'E', 'S', 'W']
d = 1
ns = 0
we = 0

way_ns = 1
way_we = 10
t_ns = 1
t_we = 10

for ins in nav:
    if ins[:1] == 'N' or ins[:1] == 'E' or ins[:1] == 'S' or ins[:1] == 'W':
        if ins[:1] == 'N':
            way_ns += int(ins[1:])
        if ins[:1] == 'E':
            way_we += int(ins[1:])
        if ins[:1] == 'S':
            way_ns -= int(ins[1:])
        if ins[:1] == 'W':
            way_we -= int(ins[1:])

    elif ins[:1] == 'L' or ins[:1] == 'R':
        turns = int(int(ins[1:])/90)
        t_ns = way_ns
        t_we = way_we

        if turns == 2:
            way_ns *= -1
            way_we *= -1
        elif ins[:1] == 'L':
            if turns == 1:
                way_we = t_ns*-1
                way_ns = t_we
            if turns == 3:
                way_we = t_ns
                way_ns = t_we*-1
        elif ins[:1] == 'R':
            if turns == 1:
                way_we = t_ns
                way_ns = t_we*-1
            if turns == 3:
                way_we = t_ns*-1
                way_ns = t_we

    elif ins[:1] == 'F':
        ns += way_ns*int(ins[1:])
        we += way_we*int(ins[1:])

print(ns, we)