
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
    

def p2(x):
    pass

if __name__ == "__main__":
    g = []
    with open("input.txt", "r") as f:
        line = f.readline().strip().split()
        while line != []:
            g.append(line)
            line = f.readline().strip().split()
    p1(g)