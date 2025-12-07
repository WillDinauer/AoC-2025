def update_row(row, beams):
    next_beams = set()
    split = 0
    for b in beams:
        if row[b] == 1:
            split += 1

            for cand in [b-1, b+1]:
                if cand >= 0 and cand < len(row):
                    next_beams.add(cand)
        else:
            next_beams.add(b)
    
    return split, next_beams

def p1(g, start):
    beams = {start}
    split = 0
    for row in g:
        num_split, beams = update_row(row, beams)
        split += num_split
    print(split)

def p2(g, start):
    # memoize
    seen = {}
    def recurse(r, c):
        # base case
        if r == len(g)-1:
            return 1
        
        # use prev work
        if (r,c) in seen:
            return seen[(r, c)]
        
        # recurse top to bottom
        if g[r][c] == 1:
            res = recurse(r+1, c-1) + recurse(r+1, c+1)
        else:
            res = recurse(r+1, c)

        seen[(r, c)] = res
        return res
    result = recurse(0, start)
    print(result)
        

if __name__ == "__main__":
    g = []
    start = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            cur = [0] * len(line)
            for i in range(len(line)):
                match line[i]:
                    case ".":
                        cur[i] = 0
                    case "^":
                        cur[i] = 1
                    case "S":
                        start = i
            g.append(cur)
    p1(g, start)
    p2(g, start)