import math

def p1(g):
    res = 0
    for c in range(len(g[0])):
        mult = g[-1][c] == "*"
        cur = 1 if mult else 0
        for r in range(len(g)-1):
            if mult:
                cur *= int(g[r][c])
            else:
                cur += int(g[r][c])
        res += cur
    print(res)
    

def p2(g):
    res = 0
    vals = []
    for c in range(len(g[0])-1, -1, -1):
        empty = True
        for r in range(len(g)-1):
            if g[r][c] != " ":
                empty = False
                break
        
        if empty:
            res += sum(vals) if g[-1][c+1] == "+" else math.prod(vals)
            vals = []
            continue

        cur = 0
        for r in range(len(g)-1):
            if g[r][c] != " ":
                cur *= 10
                cur += int(g[r][c])
        vals.append(cur)
    res += sum(vals) if g[-1][0] == "+" else math.prod(vals)
    print(res)


if __name__ == "__main__":
    filename = "input.txt"
    g = []
    with open(filename, "r") as f:
        line = f.readline().strip().split()
        while line != []:
            g.append(line)
            line = f.readline().strip().split()
    p1(g)

    with open(filename, "r") as f:
        g = [line.strip("\n") for line in f.readlines()]
    p2(g)