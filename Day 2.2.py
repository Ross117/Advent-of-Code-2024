with open('input.txt') as file:
    input = file.read().split('\n')

input_lists: list[list[int]] = [[int(val) for val in val.split(' ')] for val in input]

def safe(report) -> bool | None:
    '''Check if the report is safe.
    Return true if in the given list, the numeric values are both:
    - all increasing, or all descreasing
    - Any two adjacent values differ by at least one and at most three
    Otherwise, return false'''

    if report == sorted(report) or report == sorted(report, reverse=True):
    
        for ind, level in enumerate(report):
            if ind == len(report) - 1:
                break
            if abs(level - report[ind + 1]) > 3 or level == report[ind + 1]:
                return False
        return True


safe_reports: int = 0

for report in input_lists:
    if safe(report):
        safe_reports += 1
    else:
        # test the report with one value removed, looping through all options
        for ind, level in enumerate(report):
            new_report: list[int] = report.copy()
            new_report.pop(ind)
            if safe(new_report):
                safe_reports += 1
                break

answer = safe_reports
print(answer)