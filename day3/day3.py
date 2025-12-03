def p1(x):
    res = 0
    for line in x:
        best = 0
        for i in range(len(line)-1):
            for j in range(i+1, len(line)):
                cur = line[i]*10 + line[j] 
                if cur > best:
                    best = cur
        res += best
    print(res)

def recurse(line, index, x, val):
    if x == 0:
        return val
    best = line[index]
    bp = index
    for i in range(index, len(line) - x + 1):
        if line[i] > best:
            best = line[i]
            bp = i
    val = (val * 10) + best
    return recurse(line, bp+1, x-1, val)

def p2(x):
    res = 0
    for line in x:
        res += recurse(line, 0, 12, 0)
    print(res)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    x = []
    for line in lines:
        l = []
        for i in range(len(line)):
            l.append(int(line[i]))
        x.append(l)
    p1(x)
    p2(x)