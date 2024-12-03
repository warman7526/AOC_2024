import re

#define a regex pattern to search for valid mul(a,b) statements
match_pattern = r"mul\(\d+,\d+\)"

#read the file data
with open("day3/data.txt", "r") as f:
    data = f.read()

#strip the mul statements into pairs of values to be multiplied
muls = [[int(val) for val in match[4:-1].split(',')] for match in re.findall(match_pattern, data)]

#calculate the multiplications and get the sum
res = sum([mul[0] * mul[1] for mul in muls])

print(res)
