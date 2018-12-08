from functools import reduce
from collections import namedtuple

Node = namedtuple("Node", "children metadata")

def parse_node(data):
    child_count, metadata_count, *data = data
    children = []
    for i in range(child_count):
        child, data = parse_node(data)
        children += [child]
    metadata = data[:metadata_count]
    return Node(children, metadata), data[metadata_count:]

def sum_part1(node):
    return sum(node.metadata) + sum([sum_part1(child) for child in node.children])

def sum_part2(node):
    if node.children:
        return sum([sum_part2(node.children[idx - 1]) for idx in node.metadata if idx and idx <= len(node.children)])
    else:
        return sum(node.metadata)

data = list(map(int, open("input.txt").readlines()[0].split()))
root, _ = parse_node(data)

print(sum_part1(root))
print(sum_part2(root))