
def p1(x):
    res = 0
    for r in x:
        arr = r.split("-")
        small = int(arr[0])
        large = int(arr[1])
        for i in range(small, large+1):
            ns = str(i)
            if len(ns) % 2 != 0:
                continue
            mid = int(len(ns) / 2)
            if ns[:mid] == ns[mid:]:
                res += i
    print(res)

def windowed_check(x, is_odd):
    step = 2 if is_odd else 1
    divisor = 3 if is_odd else 2
    for ws in range(1, int(len(x) / divisor) + 1, step):
        if len(x) % ws != 0:
            continue
        window = x[:ws]
        failed = False
        for i in range(ws, len(x), ws):
            if window != x[i:i+ws]:
                failed = True
                break
        if not failed:
            return True
    return False

def p2(x):
    res = 0
    for r in x:
        arr = r.split("-")
        small = int(arr[0])
        large = int(arr[1])
        for i in range(small, large+1):
            num_string = str(i)
            if (len(num_string) % 2 == 0 and windowed_check(num_string, is_odd=False)) or \
               (len(num_string) % 2 != 0 and windowed_check(num_string, is_odd=True)):
                res += i
    print(res)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        arr = f.readline().strip().split(",")
    p1(arr)
    p2(arr)