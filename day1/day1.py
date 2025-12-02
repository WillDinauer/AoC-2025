SIZE = 100
START = 50

def p1(lines):
    res = 0
    pos = START
    for line in lines:
        input = line.strip()
        val = int(input[1:])
        if input[:1] == "L":
            val = SIZE - val
        pos = (pos + val) % SIZE
        if pos == 0:
            res += 1

    print(f"p1: {res}")

def p2(lines):
    res = 0
    pos = START
    prev = pos
    for line in lines:
        input = line.strip()

        # Handle large values
        val = int(input[1:])
        full_rots = int (val / SIZE)
        res += full_rots
        val %= SIZE

        # Which direction to rotate
        if input[:1] == "L":
            pos -= val
        else:
            pos += val

        # Don't extra count if we started on 0...
        if prev != 0 and (pos >= SIZE or pos <= 0):
            res += 1

        # Prep for next input
        pos %= SIZE
        prev = pos
    print(f"p2: {res}")


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
    p1(lines)
    p2(lines)