def start(str):
    return str[0]

def end(str):
    return str[-1]

def verify(x, chrs):
    for y in chrs:
        z = []
        for i in range(3):
            if y[i] in x:
                z.append(x.index(y[i]))

        if not all(z[i] <= z[i + 1] for i in range(len(z) - 1)):
            return False

    return True

chrs = []

with open("passcharacters.txt", encoding = "utf-8") as f:
    for line in f:
        line = line.strip()
        if line not in chrs:
            chrs.append(line)

x = chrs.pop(0)

while len(chrs) is not 0:
    for y in chrs:
        if y[0] in x and y[1] in x and y[2] in x:
            chrs.remove(y)

        elif y[0] in x and y[2] in x:
            for z in range(x.index(y[2]) - x.index(y[0])):
                t = x[:x.index(y[0]) + 1 + z] + y[1] + x[x.index(y[0]) + 1 + z:]
                if (verify(t, chrs) == True):
                    x = t
                    break

        elif y[0] in x and y[1] in x:
            if end(x) == y[1]:
                x = x + y[2]
                chrs.remove(y)

        elif y[1] in x and y[2] in x:
            if start(x) == y[1]:
                x = y[0] + x
                chrs.remove(y)

        elif start(x) == end(y):
            x = y[:2] + x
            chrs.remove(y)

        elif end(x) == start(y):
            x = x + y[1:]
            chrs.remove(y)

print(x)
