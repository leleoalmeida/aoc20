forms = open("input.txt").read()
forms = [x.split() for x in forms.split('\n\n') if x.split()]
print(forms)

unique = [''] * len(forms)


#SECOND HALF
for i, groups in enumerate(forms):
    if len(forms[i]) == 1:
        unique[i] += forms[i][0]
    else:
        for char in forms[i][0]:
            boolean = True
            for j, answer in enumerate(forms[i][1:]):            
                if char not in answer:
                    boolean = False
            if boolean:
                unique[i] += char

for i, x in enumerate(unique):
    unique[i] = len(x)

print(sum(unique))


#FIRST HALF
'''
for i, groups in enumerate(forms):
    for answer in forms[i]:
        for char in answer:
            if char not in unique[i]:
                unique[i] += char

for i, x in enumerate(unique):
    unique[i] = len(x)

print(sum(unique))
'''