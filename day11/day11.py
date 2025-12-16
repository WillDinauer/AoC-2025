
def p1(g, labels):
    end = labels["out"]
    start = labels["you"]
    visited = [0] * len(labels)
    visited[end] = 1

    def recurse(val):
        # base case
        if visited[val] > 0:
            return visited[val]
        
        # recurse over all out connections
        res = 0
        for out_con in g[val]:
            res += recurse(out_con)
        
        # memoize
        visited[val] = res
        return res
    
    res = recurse(start)

    print(res)

def p2(g, labels):
    end = labels["out"]
    start = labels["svr"]
    dac = labels["dac"]
    fft = labels["fft"]

    visited = [[0] * len(labels)] * 4
    dac_visited = 1
    fft_visited = 2
    two_visited = 3

    visited[two_visited][end] = 1

    def recurse(val, seen):
        if visited[seen][val] > 0:
            return visited[seen][val]
        
        if val == dac:
            if seen == two_visited:
                raise RuntimeError("I wouldn't expect this to be possible.")
            if seen == fft_visited:
                seen = two_visited
            else:
                seen = dac_visited
        
        if val == fft:
            if seen == two_visited:
                raise RuntimeError("I wouldn't expect this to be possible.")
            if seen == fft_visited:
                seen = two_visited
            else:
                seen = fft_visited

        res = 0
        for out_con in g[val]:
            res += recurse(out_con, seen)
        visited[seen][val] = res
        return res
    
    res = recurse(start, 0)
    print(res)

if __name__ == "__main__":
    g = {}
    cur = 0
    labels = {}
    with open("sample.txt", "r") as f:
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
    p1(g, labels)

    with open("sample2.txt", "r") as f:
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