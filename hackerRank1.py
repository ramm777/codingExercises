# https://www.hackerrank.com/challenges/
# This is Problem Solving kit


import math
def gradingStudents(grades):
    """
    https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
    """
    ngrades = []
    for i in grades:
        if i < 38:
            ngrades.append(i)
        else:
            next_multiple = math.ceil(i / 5) * 5
            if next_multiple - i < 3:
                new_number = next_multiple
            else:
                new_number = i
            ngrades.append(new_number)

    return ngrades

#grades_count = int(input().strip())
#grades = []
#for _ in range(grades_count):
#    grades_item = int(input().strip())
#    grades.append(grades_item)
#result = gradingStudents(grades)


def diagonalDifference(arr):
    """
    https://www.hackerrank.com/challenges/diagonal-difference/problem
    """
    n = len(arr)

    diag_l = 0
    diag_r = 0
    for i, j in zip(range(0, n), range(n - 1, -1, -1)):
        diag_l = diag_l + arr[i][i]
        diag_r = diag_r + arr[i][j]
    result = abs(diag_l - diag_r)

    return result

#n = int(input().strip())
#arr = []
#for _ in range(n):
#    arr.append(list(map(int, input().rstrip().split())))
#result = diagonalDifference(arr)

def miniMaxSum(arr):
    sum_arr = []
    for i in range(len(arr)):
        # itself = arr[i]
        others = arr[:i] + arr[i + 1:]
        sum_arr.append(sum(others))

        result = str(min(sum_arr)) + " " + str(max(sum_arr))

    return print(result)

#miniMaxSum([1, 3, 5, 7, 9])

