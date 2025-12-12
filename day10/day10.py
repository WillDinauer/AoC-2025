def p1(p, b):
    

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