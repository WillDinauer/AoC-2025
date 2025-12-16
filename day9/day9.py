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

# ------ P2 -------
dirs = {
    "left": 0,
    "right": 1,
    "up": 2,
    "down" : 3
}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

horizontal = []
vertical = []
outside = {}
debug = False

# Check if the pt rests on a line
def on_line(pt):
    for line in horizontal:
        if pt[1] == line[0] and line[1] <= pt[0] <= line[2]:
            return True
    
    for line in vertical:
        if pt[0] == line[0] and line[1] <= pt[1] <= line[2]:
            return True
    return False

def vert_check(pt):
    out = True
    x = pt[0]
    y = pt[1]
    for line in horizontal:
        if line[0] > y:
            return out
        
        # Crossing line
        if line[1] < x < line[2]:
            out = not out
        
        # Check corner hit
        if line[1] == x:
            out = dirs["down"] in outside[tuple([line[1], line[0]])]

        if line[2] == x:
            out = dirs["down"] in outside[tuple([line[2], line[0]])]
    return out

def horiz_check(pt):
    out = True
    x = pt[0]
    y = pt[1]
    for line in vertical:
        if line[0] > x:
            return out
        
        if line[1] < y < line[2]:
            out = not out

        if line[1] == y:
            out = dirs["right"] in outside[tuple([line[0], line[1]])]
        
        if line[2] == y:
            out = dirs["right"] in outside[tuple([line[0], line[2]])]
    return out

def h_line_check(y, x0, x1):
    for line in vertical:
        if line[0] < x0:
            continue
        if line[0] >= x1:
            return True
        if line[0] == x0:
            if tuple([line[0], y]) in outside and dirs["right"] in outside[tuple([line[0], y])]:
                return False
            continue
        if line[1] < y < line[2]:
            return False
        if line[1] == y or line[2] == y:
            if len(outside[tuple([line[0], y])]) != 0:
                return False
    return True

def v_line_check(x, y0, y1):
    for line in horizontal:
        if line[0] < y0:
            continue
        if line[0] >= y1:
            return True
        if line[0] == y0:
            if tuple([x, line[0]]) in outside and dirs["down"] in outside[tuple([x, line[0]])]:
                return False
            continue
        if line[1] < x < line[2]:
            return False
        if line[1] == x or line[2] == x:
            if len(outside[tuple([x, line[0]])]) != 0:
                return False
    return True


def clean(a, b):
    return v_line_check(a[0], min(a[1], b[1]), max(a[1], b[1])) if a[0] == b[0] else h_line_check(a[1], min(a[0], b[0]), max(a[0], b[0]))

def line_checks(a, b, c, d):
    return clean(a, c) and clean(a, d) and clean(b, c) and clean(b, d)

# Check if the pt is inside the figure
def inside(pt):
    if on_line(pt):
        return True
    vc = not vert_check(pt)
    hc = not horiz_check(pt)
    if vc != hc:
        raise RuntimeError("WHAT????")
    return vc

def get_dir(a, b):
    if a[0] == b[0]:
        return dirs["down"] if a[1] < b[1] else dirs["up"]
    return dirs["left"] if a[0] > b[0] else dirs["right"]

def get_outside(cur, after):
    swap = False
    up = "down" if swap else "up"
    down = "up" if swap else "down"
    right = "left" if swap else "right"
    left = "right" if swap else "left"
    if cur == dirs["down"]:
        return [] if after == dirs[right] else [dirs["down"], dirs[right]]
    if cur == dirs["up"]:
        return [] if after == dirs[left] else [dirs["up"], dirs[left]]
    if cur == dirs["right"]:
        return [] if after == dirs[up] else [dirs[up], dirs["right"]]
    if cur == dirs["left"]:
        return [] if after == dirs[down] else [dirs[down], dirs["left"]]
    
    raise RuntimeError(f"Invalid direction provided to get_outside(): {cur}")

def p2(pts):
    # Compute horizontal, vertical, and directions
    direction = get_dir(pts[-1], pts[0])
    for i, pt in enumerate(pts):
        after = pts[i+1] if i < len(pts)-1 else pts[0]
        next_dir = get_dir(pt, after)

        outside[tuple(pt)] = get_outside(direction, next_dir)
        direction = next_dir

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
            if inside(c1) and inside(c2):
                if line_checks(a, b, c1, c2):
                    if ar > best:
                        best = ar
    print(best)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        pts = [[int(x) for x in line.strip().split(",")] for line in f.readlines()]
    p1(pts)
    p2(pts)