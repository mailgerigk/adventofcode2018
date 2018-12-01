with open("input.txt") as f: 
    lines = f.readlines();
    
a = [int(n) for n in lines];
i = 0
d = {}
f = 0
while f not in d:
    d[f] = 0
    f += a[i]
    i = (i + 1) % len(a)
print(f)