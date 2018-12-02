with open("input.txt") as f:
    lines = f.readlines()

_2 = 0
_3 = 0

for line in lines:
    _2counted = False
    _3counted = False
    for c in line:
        if not _2counted and line.count(c) == 2:
            _2counted = True
            _2 += 1
        if not _3counted and line.count(c) == 3:
            _3counted = True
            _3 += 1

print(_2 * _3)