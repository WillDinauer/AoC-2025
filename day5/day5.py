def p1(ranges, inputs):
    res = 0
    for x in inputs:
        for r in ranges:
            if x >= r[0] and x <= r[1]:
                res += 1
                break
    print(res)

def p2(ranges):
    ordered = sorted(ranges, key=lambda x: x[0])
    result = 0
    cur = ordered[0]
    for i in range(1, len(ordered)):
        x = ordered[i]
        if cur[1] < x[0]:
            result += (cur[1]-cur[0] + 1)
            cur = x
        else:
            cur[1] = max(x[1], cur[1])
    result += (cur[1]-cur[0] + 1)
    print(result)


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
    p2(ranges)