import heapq

############
#### P1 ####
############

def press(cur, button):
    for idx in button:
        cur[idx] = (cur[idx] + 1) % 2
    return cur

def check(cur, p):
    for i in range(len(cur)):
        if cur[i] != p[i]:
            return False
    return True

def solve(p, b):
    seen = set()
    start = [0 for _ in range(len(p))]
    q = [[start, 0]]

    while len(q) > 0:
        cur, depth = q.pop(0)
        if tuple(cur) in seen:
            continue
        seen.add(tuple(cur))
        
        if check(cur, p):
            return depth
        
        for button in b:
            sequence = press(cur.copy(), button)
            q.append([sequence, depth + 1])
    
    raise RuntimeError("no solution found??")

def p1(p, b):
    res = 0
    for i in range(len(p)):
        res += solve(p[i], b[i])
    print(res)


############
#### P2 ####
############

class CustomItem:
    def __init__(self, pattern, cur, depth):
        self.cur = cur
        self.depth = depth
        self.priority = distance(pattern, cur)

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        if self.priority == other.priority:
            return self.depth < other.depth
        return False
    
    def __repr__(self):
        return f"CustomItem(cur={self.cur}, depth='{self.depth}', priority={self.priority})"

def distance(pattern, candidate):
    dist = 0
    for i in range(len(pattern)):
        dist += pattern[i] - candidate[i]
    return dist

def press_p2(cur, button):
    for idx in button:
        cur[idx] += 1
    return cur

def over(v, cur):
    for i in range(len(v)):
        if cur[i] > v[i]:
            return True
    return False

def solve_p2(v, b):
    seen = set()
    start = [0 for _ in range(len(v))]
    pq = []
    heapq.heappush(pq, CustomItem(v, start, 0))

    while len(pq) > 0:
        item = heapq.heappop(pq)
        cur = item.cur
        depth = item.depth

        if over(v, cur) or tuple(cur) in seen:
            continue
        seen.add(tuple(cur))
        
        if check(cur, v):
            return depth
        
        for button in b:
            sequence = press_p2(cur.copy(), button)
            heapq.heappush(pq, CustomItem(v, sequence, depth + 1))

    raise RuntimeError("no solution found??")


def p2(v, b):
    res = 0
    for i in range(len(v)):
        res += solve_p2(v[i], b[i])
        print(f"finished {i}")
    print(res)

if __name__ == "__main__":
    patterns = []
    buttons = []
    voltages = []
    with open("input.txt", "r") as f:
        line = f.readline().strip().split()
        while line != []:
            pattern = [0 if line[0][i] == "." else 1 for i in range(1, len(line[0])-1)]
            button_set = []
            for i in range(1, len(line)-1):
                button = [int(x) for x in line[i][1:len(line[i])-1].split(",")]
                button_set.append(button)
            voltage = [int(x) for x in line[-1][1:len(line[-1])-1].split(",")]

            patterns.append(pattern)
            buttons.append(button_set)
            voltages.append(voltage)
            
            line = f.readline().strip().split()

    p1(patterns, buttons)
    p2(voltages, buttons)