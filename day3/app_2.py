import re

# define a regex pattern to search for valid mul(a,b),do(), and don't() statements
match_pattern = r"((mul\(\d+,\d+\))|(do(n't)?\(\)))"

# read the file data
with open("day3/data.txt", "r") as f:
    data = f.read()

statements = [match[0] for match in re.findall(match_pattern, data)]  # find all valid statements with the regex (get the match of group 0)
muls = []  # this array will store muls that are not disabled
disabled = False  # disabled flag

# loop trough each statement and run the appropriate action
for statement in statements:
    # update the flag after a do()/don't()
    if statement == "don't()":
        disabled = True
    elif statement == "do()":
        disabled = False
    # add [a,b] to muls, where a & b are the values to be multiplied
    elif not disabled:
        muls.append([int(val) for val in statement[4:-1].split(",")])

# calculate the multiplications and get the sum
res = sum([mul[0] * mul[1] for mul in muls])

print(res)
