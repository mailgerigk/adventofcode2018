with open("input.txt") as f:
    lines = f.readlines()

# part 1
line = lines[0].strip()
count = len(line) + 1
while count != len(line):
    count = len(line)
    for i in range(ord('z') - ord('a') + 1):
        line = line.replace(chr(i + ord('a')) + chr(i + ord('A')), "")
        line = line.replace(chr(i + ord('A')) + chr(i + ord('a')), "")

print(len(line))

# part 2
best_count = len(lines[0])
for c in range(ord('z') - ord('a') + 1):
    line = lines[0].strip().replace(chr(c + ord('a')), "").replace(chr(c + ord('A')), "")
    count = len(line) + 1
    while count != len(line):
        count = len(line)
        for i in range(ord('z') - ord('a') + 1):
            line = line.replace(chr(i + ord('a')) + chr(i + ord('A')), "")
            line = line.replace(chr(i + ord('A')) + chr(i + ord('a')), "")
    if count < best_count:
        best_count = count

print(str(best_count))