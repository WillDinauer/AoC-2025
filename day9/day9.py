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


def p2(pts):
    # Calculate grid size
    mx = 0
    my = 0
    for pt in pts:
        if pt[0] > mx:
            mx = pt[0]
        if pt[1] > my:
            my = pt[1]

    grid = [[0 for _ in range(mx+1)] for _ in range(my+1)]

    # Draw a line in the grid from point 'a' to point 'b'
    def draw_line(a, b):
        nonlocal grid
    
        min_c = min(a[0], b[0])
        max_c = max(a[0], b[0])

        min_r = min(a[1], b[1])
        max_r = max(a[1], b[1])

        for r in range(min_r, max_r + 1, 1):
            for c in range(min_c, max_c + 1, 1):
                grid[r][c] = 1
    
    # Paint borders
    for i, pt in enumerate(pts):
        next = pts[i+1] if i < len(pts) - 1 else pts[0]
        draw_line(pt, next)
    
    # Paint inner section
    for r in range(len(grid)):
        on = False
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                on = not on
            if on:
                grid[r][c] = 1
    
    print(grid)




if __name__ == "__main__":
    with open("input.txt", "r") as f:
        pts = [[int(x) for x in line.strip().split(",")] for line in f.readlines()]
    p1(pts)
    p2(pts)