# reads data as 2d array
with open("day2/data.txt", "r") as f:
    data = [[int(num) for num in line.split()] for line in f.readlines()]

# function to determine the sign of a number
sign = lambda x: 0 if x == 0 else (1 if x > 0 else -1)


#generate all verisons of the array with one elment removed
def dampen(arr):
    res = []
    for i in range(len(arr)):
        res.append(arr[:i]+arr[i+1:])
    return res


# determines if a given report is safe
def is_safe(arr):

    # fills diff with the steps between each pari of levels
    diffs = []
    for i in range(len(arr) - 1):
        diffs.append(arr[i] - arr[i + 1])

    # return False if there are both increases and decreases in the report
    if sign(max(diffs)) != sign(min(diffs)):
        return False
    

    # return False if there is more than difference outside of the acceptable range
    if sum([abs(diff) > 3 or abs(diff) < 1 for diff in diffs]):
        return False

    # otherwise, return True
    return True

def is_safe_damp(arr):
    for test in dampen(arr):
        if is_safe(test): return True
    return False


# scan each report in the data to check if it is safe and print the total number of safe reports
safe_reports = [is_safe_damp(report) for i,report in enumerate(data)]
print(sum(safe_reports))