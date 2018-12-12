from collections import namedtuple

def are_eq(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

Rule = namedtuple("Rule", "expression result")

with open("input.txt") as f:
    lines = f.readlines()

inital_state = lines[0].split(":")[1].strip()

rules = []
for r in lines[2:]:
    parts = r.split("=>")
    rules += [Rule(parts[0].strip(), parts[1].strip())]

pots = ["." for i in range(len(inital_state) * 10)] + list(inital_state) + ["." for i in range(len(inital_state) * 10)]
new_pots = ["." for i in range(len(pots))]

for g in range(20):
    for i in range(len(pots) - 5):
        for r in rules:
            if are_eq(r.expression, pots[i:i+5]):
                new_pots[i+2] = r.result
                break
    pots, new_pots = new_pots, ["." for i in range(len(pots))]

s = 0
for i in range(len(pots)):
    if pots[i] == "#":
        s += i - len(inital_state) * 10

prev_s = 0
prev_diff = 0
for g in range(50000000000):
    for i in range(len(pots) - 5):
        for r in rules:
            if are_eq(r.expression, pots[i:i+5]):
                new_pots[i+2] = r.result
                break
    pots, new_pots = new_pots, ["." for i in range(len(pots))]
    s = 0
    for i in range(len(pots)):
        if pots[i] == "#":
            s += i - len(inital_state) * 10
    diff = s - prev_s
    if diff == prev_diff:
        print((50000000000 - (g-1)) * diff + s)
    prev_diff = diff
    prev_s = s

