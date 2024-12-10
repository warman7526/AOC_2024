##THIS WILL EVENTUALLY WORK, BUT NGL PROBABLY AFTER THE HEAT DEATH OF THE UNIVERSE :p
##I WILL PROBABLY FIX AT SOME POINT BUT I HAVE NO TIME RN lol

import itertools, math

with open("day5/data.txt", "r") as f:
    data = f.read().split("\n\n")

rules = [rule.split("|") for rule in data[0].split("\n")]
updates = [update.split(",") for update in data[1].split("\n")]


def is_valid(i, update):
    print("validating update", i)
    valid_rules = [rule for rule in rules if (rule[0] in update and rule[1] in update)]
    positions = {}
    for page in update:
        positions[page] = update.index(page)

    for rule in valid_rules:
        if positions[rule[0]] > positions[rule[1]]:
            return False

    return True


def middle_page(update):
    return int(update[len(update) // 2])


def corrected(i, update):
    print("correcting update", i)
    permutations = itertools.permutations(update)
    for j in range(math.factorial(len(update))):
        if is_valid(str(i) + "." + str(j), t := next(permutations)):
            return t
    return None


corrected_updates = [
    corrected(i, update) for i, update in enumerate(updates) if not is_valid(i, update)
]

middle_pages = [middle_page(update) for update in corrected_updates]
print(f"{middle_pages=}\n{sum(middle_pages)=}")
