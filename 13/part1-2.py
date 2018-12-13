from collections import namedtuple
from enum import Enum

class Direction(Enum):
    Up = "^"
    Down = "v"
    Left = "<"
    Right = ">"

class TrackType(Enum):
    Null = " "
    Vertical = "|"
    Horizontal = "-"
    TopLeft = "/"
    BottomLeft = "\\"
    Crossing = "+"

def is_track(c):
    return " |-/\\+".count(c) > 0

def is_dir(c):
    return "^v<>".count(c) > 0

def sym2track(c):
    return [TrackType.Null, TrackType.Vertical, TrackType.Horizontal, TrackType.TopLeft, TrackType.BottomLeft, TrackType.Crossing][" |-/\\+".index(c)]

def sym2dir(c):
    return [Direction.Up, Direction.Down, Direction.Left, Direction.Right]["^v<>".index(c)]

def dir2vec(dir):
    if dir == Direction.Left:
        return (-1, 0)
    if dir == Direction.Right:
        return (+1, 0)
    if dir == Direction.Up:
        return (0, -1)
    return (0, +1)

def dir2track(dir):
    if dir == Direction.Left or dir == Direction.Right:
        return TrackType.Horizontal
    return TrackType.Vertical

def rotate(mdir, cdir):
    if cdir == Direction.Left:
        if mdir == Direction.Up:
            return Direction.Left
        if mdir == Direction.Down:
            return Direction.Right
        if mdir == Direction.Left:
            return Direction.Down
        return Direction.Up
    if cdir == Direction.Right:
        if mdir == Direction.Up:
            return Direction.Right
        if mdir == Direction.Down:
            return Direction.Left
        if mdir == Direction.Left:
            return Direction.Up
        return Direction.Down
    return mdir

def next_cdir(cdir):
    a = [Direction.Left, Direction.Up, Direction.Right]
    return a[(a.index(cdir) + 1) % 3]

def track2dir(track, dir, cdir):
    if track == TrackType.Vertical or track == TrackType.Horizontal:
        return dir, cdir
    if track == TrackType.TopLeft:
        if dir == Direction.Up:
            return Direction.Right, cdir
        if dir == Direction.Left:
            return Direction.Down, cdir
        if dir == Direction.Down:
            return Direction.Left, cdir
        return Direction.Up, cdir
    if track == TrackType.BottomLeft:
        if dir == Direction.Up:
            return Direction.Left, cdir
        if dir == Direction.Left:
            return Direction.Up, cdir
        if dir == Direction.Down:
            return Direction.Right, cdir
        return Direction.Down, cdir
    return rotate(dir, cdir), next_cdir(cdir)

def tick_state(tracks, carts):
    skip_list = []
    collisions = []
    for y in range(len(carts)):
        for x in range(len(carts[y])):
            if not carts[y][x]:
                continue
            if skip_list.count((y,x)) > 0:
                continue
            dx, dy = dir2vec(carts[y][x][0])
            dx, dy = x + dx, y + dy
            if carts[dy][dx]:
                collisions += [(dx, dy)]
                carts[dy][dx] = None
                carts[y][x] = None
            else:
                carts[dy][dx] = track2dir(tracks[dy][dx], carts[y][x][0], carts[y][x][1])
                carts[y][x] = None
                skip_list += [(dy, dx)]
    return collisions

def print_state(tracks, carts):
    for y in range(len(carts)):
        for x in range(len(carts[y])):
            if not carts[y][x]:
                print(end=tracks[y][x].value)
            else:
                print(end=carts[y][x][0].value)
        print()

with open("input.txt") as f:
    lines = f.readlines()

tracks = [[sym2track(c) if not is_dir(c) else dir2track(sym2dir(c)) for c in line if c != "\n"] for line in lines]
carts = [[None if not is_dir(c) else (sym2dir(c), Direction.Left) for c in line if c != "\n"] for line in lines]

ticks = 0
collisions = []
while not len(collisions):
    ticks += 1
    collisions = tick_state(tracks, carts)
    #print_state(tracks, carts)

print(collisions)

while len([0 for y in range(len(carts)) for x in range(len(carts[y])) if carts[y][x]]) > 1:
    ticks += 1
    collisions = tick_state(tracks, carts)
    if len(collisions):
        print(collisions)
    #print_state(tracks, carts)

print([(x,y) for y in range(len(carts)) for x in range(len(carts[y])) if carts[y][x]])