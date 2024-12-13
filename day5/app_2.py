import itertools, math

with open("day5/data.txt", "r") as f:
    data = f.read().split("\n\n")

rules = [rule.split("|") for rule in data[0].split("\n")]
updates = [update.split(",") for update in data[1].split("\n")]


def is_valid(i, update):
    if i != -1:
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


def correct(n, update):
    print("correcting update", n)

    def correction_step(placed: list, remaining: list):
        for i, item in enumerate(remaining):
            for pos in range(len(placed) + 1):
                test = placed.copy()
                test.insert(pos, item)
                if is_valid(-1, test):
                    if len(test) == len(update):
                        return test
                    next = correction_step(test, remaining[:i] + remaining[i+1:])
                    if next is not None:
                        return next

    return correction_step([], update)


corrected_updates = [correct(i, update) for i,update in enumerate(updates) if not is_valid(i, update)]


middle_pages = [middle_page(update) for update in corrected_updates]
print(f"{middle_pages=}\n{sum(middle_pages)=}")