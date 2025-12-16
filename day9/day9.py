def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def p1(pts):
    best = 0
    for i, a in enumerate(pts):
        for b in pts[i+1:]:
            ar = area(a, b)
            if ar > best:
                best = ar
    print(best)

# Number of horizontal lines ABOVE the pt of interest
def above(pt, horizontal):
    res = 0
    # Line: [y, x0, x1]
    for line in horizontal:
        if line[0] > pt[1]:
            return res 
        if line[1] <= pt[0] <= line[2]:
            res += 1
    return res

# Check if the pt rests on a line
def on_line(pt, horizontal, vertical):
    for line in horizontal:
        if pt[1] == line[0] and line[1] <= pt[0] <= line[0]:
            return True
    
    for line in vertical:
        if pt[0] == line[0] and line[1] <= pt[1] <= line[0]:
            return True

# Check if the pt is inside the figure
def inside(pt, horizontal, vertical):
    if on_line(pt, horizontal, vertical): 
        return True
    return above(pt, horizontal) % 2 == 1


def p2(pts):
    # create horizontal
    horizontal = []
    vertical = []
    for i, pt in enumerate(pts):
        after = pts[i+1] if i < len(pts)-1 else pts[0] 

        # Check for horizontal lines
        if pt[1] == after[1]:
            horizontal.append([pt[1], min(pt[0], after[0]), max(pt[0], after[0])])
        else:
            vertical.append([pt[0], min(pt[1], after[1]), max(pt[1], after[1])])

    # Sort by first value in list (increasing x or y)
    horizontal.sort(key = lambda x: x[0])
    vertical.sort(key = lambda x: x[0])

    # Iterate over all pairs
    best = 0
    for i, a in enumerate(pts):
        for b in pts[i+1:]:
            # Corners
            c1 = [a[0], b[1]]
            c2 = [b[0], a[1]]
            ar = area(a, b)

            # Check if corners are inside fig, then compare
            if inside(c1, horizontal, vertical) and inside(c2, horizontal, vertical) and ar > best:
                best = ar
    print(best)

if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        pts = [[int(x) for x in line.strip().split(",")] for line in f.readlines()]
    p1(pts)
    p2(pts)