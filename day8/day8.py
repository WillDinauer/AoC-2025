import math
import heapq

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

def p1(pts, n):
    pt_mapping = {}
    groups = {}
    dists = {}
    sizes = {}
    pq = []
    for i, p1 in enumerate(pts):
        pt_mapping[p1] = i
        groups[i] = [p1]
        sizes[i] = 1
        for p2 in pts[i+1:]:
            d = distance(p1, p2)
            dists[d] = [p1, p2]
            heapq.heappush(pq, d)

    for i in range(n):
        cur = heapq.heappop(pq)
        associated_pts = dists.get(cur)
        p1 = associated_pts[0]
        p2 = associated_pts[1]

        g_index_1 = pt_mapping.get(p1)
        g_index_2 = pt_mapping.get(p2)

        # Ignore already connected pts
        if g_index_1 == g_index_2:
            continue

        s1 = sizes.get(g_index_1)
        s2 = sizes.get(g_index_2)

        g1 = groups.get(g_index_1)
        g2 = groups.get(g_index_2)
        
        for pt in g2:
            pt_mapping[pt] = g_index_1
            g1.append(pt)

        sizes[g_index_1] = s1 + s2
        sizes[g_index_2] = 0
        groups[g_index_2] = []
    
    final_sizes = []
    for s in sizes.values():
        final_sizes.append(s)
    final_sizes.sort(reverse=True)
    
    res = math.prod(final_sizes[:3])
    print(res)

def p2(pts):
    pt_mapping = {}
    groups = {}
    dists = {}
    sizes = {}
    pq = []
    for i, p1 in enumerate(pts):
        pt_mapping[p1] = i
        groups[i] = [p1]
        sizes[i] = 1
        for p2 in pts[i+1:]:
            d = distance(p1, p2)
            dists[d] = [p1, p2]
            heapq.heappush(pq, d)

    while True:
        cur = heapq.heappop(pq)
        associated_pts = dists.get(cur)
        p1 = associated_pts[0]
        p2 = associated_pts[1]

        g_index_1 = pt_mapping.get(p1)
        g_index_2 = pt_mapping.get(p2)

        # Ignore already connected pts
        if g_index_1 == g_index_2:
            continue

        s1 = sizes.get(g_index_1)
        s2 = sizes.get(g_index_2)

        if s1 + s2 == len(pts):
            print(p1[0] * p2[0])
            return

        g1 = groups.get(g_index_1)
        g2 = groups.get(g_index_2)
        
        for pt in g2:
            pt_mapping[pt] = g_index_1
            g1.append(pt)

        sizes[g_index_1] = s1 + s2
        sizes[g_index_2] = 0
        groups[g_index_2] = []


if __name__ == "__main__":
    sample = False
    file_name = "sample.txt" if sample else "input.txt"
    n = 10 if sample else 1000
    
    pts = []
    with open(file_name, "r") as f:
        line = f.readline().strip()
        while line != "":
            pt = tuple([int(x) for x in line.split(",")])
            pts.append(pt)
            line = f.readline().strip()
    
    p1(pts, n)
    p2(pts)