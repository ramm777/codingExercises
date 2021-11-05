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

def superReducedString0(s):
    """
    My implementation, not the best one as depends on the 100 loops.
    """

    for j in range(100):
        length = len(s)
        i = 0
        for i in range(length):
            if i + 1 < len(s) and s[i] == s[i+1]:
                s = s.replace(s[i], '', 2)
            else:
                continue

    if s == '': return print("Empty String")
    else:       return print(s)


def superReducedString1(s):
    """
    Solution from the internet:  https://www.youtube.com/watch?v=sKlGc3ySe9c
    """
    result = []
    for i in range(len(s)):
        if len(result)==0 or result[-1] != s[i]:
            result.append(s[i])
        else:
            result.pop()

    if len(result) == 0: return print("Empty String")
    else:                return print("".join(result))

#superReducedString0('baab')

def marsExploration(s):
    changed = 0
    for i in range(0, len(s), 3):
        if s[i:i + 3] == 'SOS':
            continue
        else:
            substr = s[i:i + 3]
            if substr[0] != 'S': changed = changed + 1
            if substr[1] != 'O': changed = changed + 1
            if substr[2] != 'S': changed = changed + 1

    return print(changed)

#marsExploration('SOSSAT')

def hackerrankInString(s):
    benchmark = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    s = list(s)
    for i in range(len(benchmark)):
        #print(s)
        if benchmark[i] in s:
            #s = s.replace(benchmark[i], '', 1)
            ind = s.index(benchmark[i])
            s = s[ind+1:].copy()
            continue
        else:
            return print('NO')

    return print('YES')

#s = 'haacckkerannkk'
#s = 'hereiamstackerrank'
#s = 'rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'
#hackerrankInString(s)

def pangrams(s):
    alpha = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
    alpha = alpha.split(', ')

    s = s.lower()
    for i in alpha:
        if i in s:
            s = s.replace(i, '', 1)
        else:
            return print('not pangram')

    return print('pangram')

#pangrams("he quick brown fox jumps over he lazy dog")
