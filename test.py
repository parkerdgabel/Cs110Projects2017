def flip_lines(name):
    file = open(name)
    if not file:
        print("Unable to open input file \"" + name + "\"!")
    lines = file.readlines()
    for i in range(len(lines) - 1):
        temp = lines[i]
        lines[i] = lines[i + 1]
        lines[i + 1] = temp
        i += 1
    for i in range(len(lines)):
        if i % 2 == 0:
            print(lines[i].upper())
        else:
            print(lines[i].lower())


def input_stats(name):
    maxChar = 0
    file = open(name)
    lines = file.readlines()
    total = 0
    counter = 1
    for line in lines:
        line_total = 0
        for char in line:
            if char != '\n':
                total += 1
                line_total += 1
        print("Line", counter, "has", line_total, "chars")
        counter += 1
        maxChar = max(maxChar, line_total)
    print(len(lines), "lines longest =", maxChar +
          ",", "average =", total / len(lines))
