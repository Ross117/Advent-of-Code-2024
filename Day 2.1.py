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
    if report == sorted(report) or report == sorted(report, reverse=True):
    
        for ind, level in enumerate(report):
            if ind == len(report) - 1:
                break
            if abs(level - report[ind + 1]) > 3 or level == report[ind + 1]:
                return 0
        return 1
    
    else:
        return 0


safe_reports: int = sum(safe(report) for report in input_lists)
answer = safe_reports
print(answer)