from collections import namedtuple
import sys

Point = namedtuple("Point", "x y")
ID = namedtuple("ID", "index distance")

with open("input.txt") as f:
    lines = f.readlines()

def distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def floodfill(grid, local_grid, index, q):
    while len(q):
        coords = q.pop(0)
        if local_grid[coords.y][coords.x] == 1 or grid[coords.y][coords.x].index != index:
            continue

        local_grid[coords.y][coords.x] = 1
        q += [Point(coords.x + 1, coords.y + 0)]
        q += [Point(coords.x - 1, coords.y + 0)]
        q += [Point(coords.x + 0, coords.y + 1)]
        q += [Point(coords.x + 0, coords.y - 1)]

def floodfill_count(grid, coords, index):
    local_grid = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
    try:
        floodfill(grid, local_grid, index, [coords])
        return sum([sum(local_grid[i]) for i in range(len(grid))])
    except:
        return 0

points = [Point(int(line.split(',')[0]), int(line.split(',')[1])) for line in lines]

min_x = min(points, key=lambda p: p.x).x
min_y = min(points, key=lambda p: p.y).y
points = [Point(p.x - min_x, p.y - min_y) for p in points]

max_x = max(points, key=lambda p: p.x).x
max_y = max(points, key=lambda p: p.y).y

grid = [[ID(-1, -1) for x in range(max_x)] for y in range(max_y)]

for index, point in enumerate(points):
    for y in range(max_y):
        for x in range(max_x):
            dist = distance(point, Point(x,y))
            if grid[y][x].index == -1 or grid[y][x].distance > dist:
                grid[y][x] = ID(index, dist)
            elif grid[y][x].distance == dist:
                grid[y][x] = ID(-2, dist)

point = max(points, key=lambda p: floodfill_count(grid, p, points.index(p)))
print(floodfill_count(grid, point, points.index(point)))

grid = [[0 for x in range(max_x)] for y in range(max_y)]

for index, point in enumerate(points):
    for y in range(max_y):
        for x in range(max_x):
            dist = distance(point, Point(x,y))
            grid[y][x] += dist

print(sum([sum([1 for x in range(max_x) if grid[y][x] < 10000]) for y in range(max_y)]))