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

'''
    # golf version
    from functools import reduce
    def parse_node(data):
        child_count, metadata_count, *data = data
        children, data = reduce(lambda a,b:(a[0]+[parse_node(a[1])[0]],parse_node(a[1])[1]),range(child_count),([],data))
        return (children, data[:metadata_count]), data[metadata_count:]
    root, _ = parse_node(list(map(int, open("input.txt").readlines()[0].split())))
    print((lambda a:lambda v:a(a,v))(lambda rec,node: sum(node[1]) + sum([rec(rec,child) for child in node[0]]))(root))
    print((lambda a:lambda v:a(a,v))(lambda rec,node: sum([rec(rec, node[0][idx - 1]) for idx in node[1] if idx and idx <= len(node[0])]) if node[0] else sum(node[1]))(root))
'''