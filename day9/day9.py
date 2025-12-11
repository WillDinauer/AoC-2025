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


def p2(x):
    pass

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        pts = [[int(x) for x in line.strip().split(",")] for line in f.readlines()]
    p1(pts)