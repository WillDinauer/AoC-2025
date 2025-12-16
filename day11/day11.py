
def p1(g, start, end, labels):
    visited = [0] * len(labels)
    visited[end] = 1

    def recurse(val):
        # base case
        if visited[val] > 0:
            return visited[val]
        
        # recurse over all 'out' connections
        res = 0

        if val in g:
            for out_con in g[val]:
                res += recurse(out_con)
        
        # memoize
        visited[val] = res
        return res
    
    res = recurse(start)

    print(res)
    return res

def p2(g, labels):
    start = labels["svr"]
    dac = labels["dac"]
    fft = labels["fft"]
    end = labels["out"]

    # num paths from svr to dac
    sd = p1(g, start, dac, labels)

    # num paths from svr to fft
    sf = p1(g, start, fft, labels)

    # num paths from fft to dac
    fd = p1(g, fft, dac, labels)

    # num paths from dac to fft
    df = p1(g, dac, fft, labels)

    # num paths from fft to out
    fo = p1(g, fft, end, labels)

    # num paths from dac to out
    do = p1(g, dac, end, labels)

    config_1 = sd * df * fo
    config_2 = sf * fd * do

    res = config_1 + config_2
    print(res)

if __name__ == "__main__":
    g = {}
    cur = 0
    labels = {}
    with open("input.txt", "r") as f:
        line = f.readline().strip().split()
        while line != []:
            line[0] = line[0][:3]
            # Relabel line
            for i, entry in enumerate(line):
                if entry not in labels:
                    labels[entry] = cur
                    cur += 1
                line[i] = labels[entry]

            # Graph construction
            g[line[0]] = line[1:]
            line = f.readline().strip().split()
    start = labels["you"]
    end = labels["out"]
    p1(g, start, end, labels)

    with open("input.txt", "r") as f:
        line = f.readline().strip().split()
        while line != []:
            line[0] = line[0][:3]
            # Relabel line
            for i, entry in enumerate(line):
                if entry not in labels:
                    labels[entry] = cur
                    cur += 1
                line[i] = labels[entry]

            # Graph construction
            g[line[0]] = line[1:]
            line = f.readline().strip().split()

    p2(g, labels)