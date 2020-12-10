adapters = open('input.txt').read().splitlines()
adapters = [int(x) for x in adapters]
adapters.sort()

adapters = adapters + [max(adapters) + 3]
current = adapters[0]

diffs =	{
  1: 1,
  2: 0,
  3: 1
}

for i, adapt in enumerate(range(0, len(adapters)-1)):
    diff = adapters[i+1] - adapters[i]
    diffs[diff] += 1


print(diffs[1]*diffs[3])

ans = {}
ans[0] = 1
for a in adapters:
    ans[a] = ans.get(a - 1, 0) + ans.get(a - 2, 0) + ans.get(a - 3, 0)

print(f'Answer: {ans[adapters[-1]]}')