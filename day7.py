lines = open("input.txt").read().splitlines()
'''
rulesb = rules

accepted = []
final = []
finalfinal = []
final3 = []
boolean = True'''

'''while boolean:
    boolean = False
    if len(accepted) == 0:
        for bags in rules:
            if 'shiny gold' in bags[1] and 'bags[0]' not in accepted:
                accepted.append(bags[0])
                boolean = True
    else:
        for i, bags in enumerate(rules):
            for acc in accepted:
                if acc in bags[1] and 'bags[0]' not in accepted:
                    accepted.append(bags[0])
                    boolean = True
                elif acc in bags[1] and 'bags[0]' in accepted:
                    accepted = accepted.pop(i)'''

            
        
    

'''
for i, bags in enumerate(rules):
    if 'shiny gold' in bags[1] and 'bags[0]' not in accepted:
        accepted.append(bags[0])
        rulesb = rules.pop(i)

for bags in rules:
    for acc in accepted:
        if acc in bags[1] and 'bags[0]' not in final:
            final.append(bags[0])

for bags in rules:
    for acc in final:
        if acc in bags[1]:
            if 'bags[0]' not in finalfinal:
                finalfinal.append(bags[0])

for bags in rules:
    for acc in finalfinal:
        if acc in bags[1]:
            if 'bags[0]' not in final3:
                final3.append(bags[0])
                                
for bags in rules:
    for acc in finalfinal:
        if acc in bags[1]:
            if 'bags[0]' not in final3:
                final3.append(bags[0])


print(len(accepted))
print(len(final))
print(len(finalfinal))
print(len(final3))'''

def rule_parser(lines):

    bag_dict = {}

    for line in lines:
        bag, _, content = line.partition(' bags contain ')

        if bag in bag_dict:
            raise ValueError(f'double {bag}')
        if content == 'no other bags.':
            content = {}
        else:
            content = content.split(', ')
            content = [c.split(' bag')[0] for c in content]
            content = {c.split(' ', 1)[1] : int(c.split(' ', 1)[0]) for c in content}

        bag_dict[bag] = content
    return bag_dict

def get_containers(rules, bag="shiny gold"):
    bags = set()
    for current_bag, content in rules.items():
        if bag in content:
            bags.add(current_bag)
            bags.update(get_containers(rules, bag=current_bag))
    return bags

print(len(get_containers(rule_parser(lines))))