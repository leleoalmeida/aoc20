lines = open("input.txt").read().splitlines()

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