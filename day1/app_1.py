data = []

# gets the data as two sorted arrays from data.txt
with open("day1/data.txt", "r") as f:
    data = [
        [int(t) for t in list(x)]
        for x in zip(*[val.split("   ") for val in f.read().split("\n")])
    ]
    data[0].sort()
    data[1].sort()


# calculates the differences between each index in the two lists
diffs = []
for i in range(len(data[0])):
    diffs.append(abs(data[0][i] - data[1][i]))

# print the total of the differences
print(sum(diffs))
