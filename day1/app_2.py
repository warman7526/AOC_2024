data = []

# gets the data as two sorted arrays from data.txt
with open("day1/data.txt", "r") as f:
    data = [
        [int(t) for t in list(x)]
        for x in zip(*[val.split("   ") for val in f.read().split("\n")])
    ]
    data[0].sort()
    data[1].sort()


# calculates the similarity score of each number in the left list
sims = []
for i, val in enumerate(data[0]):
    sims.append(data[1].count(val)*val)

# print the total of the differences
print(sum(sims))