#get puzzle input data
with open("day4/data.txt", "r") as f:
    data = f.read()


def gen_dir_strings(ws):
    # split the wordsearch into a 2d array
    ws = [list(line) for line in ws.split("\n")]
    res = []

    # arrange the values in the ws into strings representing each direction
    # that can be searched for the substring 'XMAS'

    res.append(";".join(["".join(line) for line in ws]))  # horizontal

    res.append(";".join(["".join(line) for line in zip(*ws)]))  # vertical

    # diagonals
    diagonal1 = ""
    diagonal2 = ""
    for s in range(len(ws) + len(ws[0]) - 1):
        for i in range(s + 1):
            j1 = s - i
            j2 = i - s + len(ws) - 1
            if not (i >= len(ws) or (j1 < 0 or j1 >= len(ws[0]))):
                diagonal1 += ws[i][j1]
            if not (i >= len(ws) or (j2 < 0 or j2 >= len(ws[0]))):
                diagonal2 += ws[i][j2]
        diagonal1 += ";"
        diagonal2 += ";"
    res.append(diagonal1)
    res.append(diagonal2)

    # also add the reversed versions of each
    for i in range(4):
        res.append(res[i][::-1])

    return res

#join all the directional strings together and count the instances of XMAS
print("/".join(gen_dir_strings(data)).count("XMAS"))