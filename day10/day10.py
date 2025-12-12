
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

def p2(x):
    pass

if __name__ == "__main__":
    patterns = []
    buttons = []
    voltages = []
    with open("sample.txt", "r") as f:
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