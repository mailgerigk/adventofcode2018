import re

def parse(line):
    pattern = re.compile("#(?P<id>\d*)\s*@\s*(?P<left>\d*),(?P<top>\d*):\s*(?P<width>\d*)x(?P<height>\d*)")
    match = pattern.match(line)
    id = int(match.group("id"))
    left = int(match.group("left"))
    top = int(match.group("top"))
    width = int(match.group("width"))
    height = int(match.group("height"))
    return (id, left, top, width, height)

with open("input.txt") as f:
    lines = f.readlines()

cuts = list(map(parse, lines))

cloth_width = max(map(lambda val: val[1] + val[3], cuts))
cloth_height = max(map(lambda val: val[2] + val[4], cuts))

bad_cuts = []
cloth = [[0 for x in range(cloth_width)] for y in range(cloth_height)]
for cut in cuts:
    for y in range(cut[4]):
        for x in range(cut[3]):
            cloth[cut[2] + y][cut[1] + x] += 1
            
for cut in cuts:
    for y in range(cut[4]):
        for x in range(cut[3]):
            if cloth[cut[2] + y][cut[1] + x] > 1:
                bad_cuts += [cut[0]]

good_cuts = [val[0] for val in cuts if val[0] not in bad_cuts]
print(good_cuts)
