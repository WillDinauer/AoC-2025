class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def p1(ranges, inputs):
    res = 0
    for x in inputs:
        for r in ranges:
            if x >= r[0] and x <= r[1]:
                res += 1
                break
    print(res)

def p2(x):
    pass

if __name__ == "__main__":
    ranges = []
    inputs = []
    with open("input.txt", "r") as f:
        line = f.readline().strip()
        while line != "":
            ranges.append([int(x) for x in line.split("-")])
            line = f.readline().strip()
        
        line = f.readline().strip()
        while line != "":
            inputs.append(int(line))
            line = f.readline().strip()
    p1(ranges, inputs)