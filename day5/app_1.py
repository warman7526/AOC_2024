with open("day5/data.txt", "r") as f:
    data = f.read().split("\n\n")

rules = [rule.split("|") for rule in data[0].split("\n")]
updates = [update.split(",") for update in data[1].split("\n")]


def is_valid(update):
    valid_rules = [rule for rule in rules if (rule[0] in update and rule[1] in update)]
    positions = {}
    for page in update:
        positions[page] = update.index(page)

    for rule in valid_rules:
        if positions[rule[0]] > positions[rule[1]]:
            return False
    
    return True

def middle_page(update):
    return int(update[len(update)//2])

middle_pages = [middle_page(update) for update in updates if is_valid(update)]
print(f"{middle_pages=}\n{sum(middle_pages)=}")
