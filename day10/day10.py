
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
    seen = {}

    def recurse(cur, depth):
        cur_t = tuple(cur)
        if cur_t in seen:
            if seen[cur_t] <= depth:
                return float('inf')
        seen[tuple(cur)] = depth
        
        if check(cur, p):
            return depth
        
        smallest = float('inf')
        
        for button in b:
            sequence = press(cur.copy(), button)
            val = recurse(sequence, depth + 1)
            smallest = min(smallest, val)
        return smallest
    
    cur = [0 for _ in range(len(p))]
    return recurse(cur, 0)
        

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