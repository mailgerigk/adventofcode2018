def parse_graph(lines):
    graph = {}
    for line in lines:
        req = line[5:][0]
        beg = line[36:][0]

        if not req in graph:
            graph[req] = []

        if not beg in graph:
            graph[beg] = []
        graph[beg] += [req]
        graph[beg].sort()
    return graph

with open("input.txt") as f:
    lines = f.readlines()

#part 1
graph = parse_graph(lines)
while len(graph):
    options = [c for c in graph if not len(graph[c])]
    options.sort()

    c = options[0]
    print(end=c)
    del graph[c]

    for k in graph:
        if c in graph[k]:
            graph[k].remove(c)

print()

# part 2
work_time = 60
worker_count = 5

time = 0
workers = [[] for i in range(worker_count)] 
graph = parse_graph(lines)
while len(graph) or any(map(lambda w: w != [], workers)):
    for i, w in enumerate(workers):
        if w == []:
            continue
        if w[1] <= time:
            c = w[0]
            workers[i] = []
            print(end=c)
            for k in graph:
                if c in graph[k]:
                    graph[k].remove(c)

    options = [c for c in graph if not len(graph[c])]
    while len(options) and any(map(lambda w: w == [], workers)):
        options.sort()
        c = options.pop(0)
        del graph[c]
        workers[workers.index([])] = [c, time + (1 + ord(c) - ord('A')) + work_time]
    time += 1

time -= 1

print()
print(time)