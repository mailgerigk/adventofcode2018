with open("input.txt") as f:
    lines = f.readlines()

for a in lines:
    for b in lines:
        if a == b:
            pass
        r = ""
        mismatches = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                r += a[i]
            else:
                mismatches += 1

        if mismatches == 1:
            print(r)
