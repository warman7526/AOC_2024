# reads data as 2d array
with open("day2/data.txt", "r") as f:
    data = [[int(num) for num in line.split()] for line in f.readlines()]

# function to determine the sign of a number
sign = lambda x: 0 if x == 0 else (1 if x > 0 else -1)


# determines if a given report is safe
def is_safe(arr):

    # fills diff with the steps between each pari of levels
    diffs = []
    for i in range(len(arr) - 1):
        diffs.append(arr[i] - arr[i + 1])

    # return False if there are both increases and decreases in the report
    if sign(max(diffs)) != sign(min(diffs)):
        return False

    # return False if there is a difference outside of the acceptable range
    if any([abs(diff) > 3 or abs(diff) < 1 for diff in diffs]):
        return False

    # otherwise, return True
    return True


# scan each report in the data to check if it is safe and print the total number of safe reports
safe_reports = [is_safe(report) for report in data]
print(sum(safe_reports))
