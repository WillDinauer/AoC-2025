def surrounding(g, r, c):
    res = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if (dc == 0 and dr == 0) or r + dr < 0 or r + dr >= len(g) or c + dc < 0 or c + dc >= len(g[r]):
                continue
            if g[r + dr][c + dc] == 1:
                res += 1
    return res

def p1(g):
    res = 0
    for r in range(len(g)):
        for c in range(len(g[r])):
            if g[r][c] == 1 and surrounding(g, r, c) < 4:
                res += 1
    print(res)

def p2(g):
    res = 0
    cur = -1
    while cur != 0:
        cur = 0
        for r in range(len(g)):
            for c in range(len(g[r])):
                if g[r][c] == 1 and surrounding(g, r, c) < 4:
                    cur += 1
                    g[r][c] = 0
        res += cur
    print(res)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        grid = [[0 if line[i] == "." else 1 for i in range(len(line))] \
                for line in [l.strip() for l in f.readlines()]]
    p1(grid)
    p2(grid)