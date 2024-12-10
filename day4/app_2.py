import re

with open("day4/data.txt", "r") as f:
    data = f.read()


def get_subsquares(ws, size=3):
    # split the wordsearch into an array of lines
    ws = [line for line in ws.split("\n")]
    res = []

    # fill res with all possible subsquares in the ws that are size x size
    for i in range(len(ws) - size+1):
        for j in range(len(ws[0]) - size+1):
            res.append(";".join([row[j : j + size] for row in ws[i : i + size]]))

    return res


match_cases = ["M.M;.A.;S.S", "M.S;.A.;M.S", "S.M;.A.;S.M", "S.S;.A.;M.M"]

subsquares = get_subsquares(data)

num_matches = [
    len(re.findall(match_case, "/".join(subsquares))) for match_case in match_cases
]

print(sum(num_matches))
