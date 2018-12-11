serial = int(open("input.txt").readlines()[0])

def get_power_level(x,y, serial):
    rack_id = (x+1) + 10
    power_level = rack_id * (y+1)
    power_level = power_level + serial
    power_level = power_level * rack_id
    power_level = int(power_level / 100) % 10
    power_level = power_level - 5
    return power_level

def get_nxn_sum(grid, x, y, n):
    acc = 0
    for i in range(n):
        for j in range(n):
            acc += grid[y+i][x+j]
    return acc

def get_nxn_sum_grid(grid, n):
    sum_grid = [[get_nxn_sum(grid, x, y, n) for x in range(301 - n)] for y in range(301 - n)]
    pos = (0, 0)
    value = 0
    for y in range(len(sum_grid)):
        for x in range(len(sum_grid[y])):
            if sum_grid[y][x] > value:
                pos = (1 + x, 1 + y)
                value = sum_grid[y][x]
    return (pos, value)

grid = [[get_power_level(x,y, serial) for x in range(300)] for y in range(300)]

npos, _ = get_nxn_sum_grid(grid, 3)
print(npos)

pos = (0, 0)
value = 0
size = 0

for n in range(1, 301):
    npos, nvalue = get_nxn_sum_grid(grid, n)
    if nvalue > value:
        pos = npos
        value = nvalue
        size = n

print(str(pos) + "," + str(size))

