from itertools import pairwise

with open('input.txt') as file:
    input = file.read().split('\n')

input_lists: list[list[int]] = [[int(val) for val in val.split(' ')] for val in input]

def safe(report) -> int:
    '''Check if the report is safe.
    Return true if in the given list, the numeric values are both:
    - all increasing, or all descreasing
    - Any two adjacent values differ by at least one and at most three
    Otherwise, return false'''

    # check if the values in the report are either ascending or descending
    if (report == sorted(report) or report == sorted(report, reverse=True)) \
        and all(1 <= abs(x - y) <= 3 for x, y in pairwise(report)):
        return 1
   
    return 0

safe_reports: int = sum(safe(report) for report in input_lists)
answer = safe_reports
print(answer)