import re
from collections import namedtuple

Vec2 = namedtuple("Vec2", "x y")
Obj = namedtuple("Obj", "pos, vel")

def parse_obj(line):
    pattern = re.compile("position=<\s*(?P<px>-?\d*)\s*,\s*(?P<py>-?\d*)\s*>\s*velocity=<\s*(?P<vx>-?\d*)\s*,\s*(?P<vy>-?\d*)")
    match = pattern.match(line)
    px = int(match.group("px"))
    py = int(match.group("py"))
    vx = int(match.group("vx"))
    vy = int(match.group("vy"))
    return Obj(Vec2(px, py), Vec2(vx, vy))

def print_state(objs, f):
    min_x = min(objs, key= lambda o: o.pos.x).pos.x
    max_x = 1 + max(objs, key= lambda o: o.pos.x).pos.x

    min_y = min(objs, key= lambda o: o.pos.y).pos.y
    max_y = 1 + max(objs, key= lambda o: o.pos.y).pos.y

    count_x = max_x - min_x
    count_y = max_y - min_y

    grid = [['.' for x in range(count_x)] for y in range(count_y)]

    for o in objs:
        grid[o.pos.y - min_y][o.pos.x - min_x] = '#'

    for y in range(count_y):
        for x in range(count_x):
            f.write(grid[y][x])
        f.write("\n")

def step_state(objs):
    count = 0
    delta = 1
    while True:
        old_min_x = min(objs, key= lambda o: o.pos.x).pos.x
        old_max_x = 1 + max(objs, key= lambda o: o.pos.x).pos.x

        old_min_y = min(objs, key= lambda o: o.pos.y).pos.y
        old_max_y = 1 + max(objs, key= lambda o: o.pos.y).pos.y

        old_count_x = old_max_x - old_min_x
        old_count_y = old_max_y - old_min_y

        if old_count_x > 200 or old_count_y > 200:
            delta = 10
        else:
            delta = 1

        for i in range(len(objs)):
            o = objs[i]
            objs[i] = Obj(Vec2(o.pos.x + o.vel.x * delta, o.pos.y + o.vel.y * delta), o.vel)

        count += delta

        new_min_x = min(objs, key= lambda o: o.pos.x).pos.x
        new_max_x = 1 + max(objs, key= lambda o: o.pos.x).pos.x

        new_min_y = min(objs, key= lambda o: o.pos.y).pos.y
        new_max_y = 1 + max(objs, key= lambda o: o.pos.y).pos.y

        new_count_x = new_max_x - new_min_x
        new_count_y = new_max_y - new_min_y

        if new_count_x > old_count_x or new_count_y > old_count_y:
            for i in range(len(objs)):
                o = objs[i]
                objs[i] = Obj(Vec2(o.pos.x - o.vel.x, o.pos.y - o.vel.y), o.vel)

            count -= 1
            return count
        

with open("input.txt") as f:
    lines = f.readlines()

objs = list(map(parse_obj, lines))
count = step_state(objs)
with open("output.txt", "w") as f:
    print_state(objs, f)
print(count)