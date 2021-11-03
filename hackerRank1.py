
def drawDoormat(n,m):
    '''
    Designer Door Mat excercise. This is my solution.
    However knowing the .center() function, one can do better - print("HELLO".center(11, "-"))
    '''

    rowlist = ['-' for i in range(m)]
    nestlist = [rowlist.copy() for i in range(n)]
    c = int((n-1)/2)
    c1 = int((m-1)/2)

    # Assign the centre word
    nestlist[c][c1-3 : c1+4] = ['W', 'E', 'L', 'C', 'O', 'M', 'E']

    # Assign the upper part
    item = ['.','|','.']
    ind = 1
    for i in range(0, c):
        nestlist[i][c1-ind : c1+ind+1] = item.copy()*int(len(nestlist[i][c1-ind : c1+ind+1])/3)
        ind = ind + 3

    # Assign the lower part
    ind = 1
    for i in range(n-1, c, -1):
        nestlist[i][c1-ind : c1+ind+1] = item.copy()*int(len(nestlist[i][c1-ind : c1+ind+1]) /3)
        ind = ind + 3

    for i in range(n):
        print(''.join(nestlist[i]))

    return

#ins = input().split()
#drawDoormat(int(ins[0]), int(ins[1]))


def merge_the_tools(string, k):

    substrs = []
    for i in range(0,len(string),k):
       substr = string[i:i+k]
       substrs.append(substr)
       del substr

    substrs1 = []
    for i in substrs:
        substrs1.append(''.join(dict.fromkeys(i)))

    for i in substrs1: print(i)

    return

#merge_the_tools('AABCAAADA', 3)

from collections import Counter
def wordOrder():

    # Inputs
    n = int(input())
    words = []
    for i in range(n): words.append(input())

    words_d = Counter(words)
    words_l = list(words_d.values())
    words_s = [str(x) for x in words_l]

    print(len(words_d))
    print(' '.join(words_s))

    return

# wordOrder()

def ginortS(s):

    s_l = []
    s_n = []
    s_u = []
    for i in s:
        if i.isdigit(): s_n.append(i)
        if i.islower(): s_l.append(i)
        if i.isupper(): s_u.append(i)

    s_n_odd = []
    s_n_even = []
    for i in s_n:
        i = int(i)
        if i%2 == 0: s_n_even.append(str(i))
        else: s_n_odd.append(str(i))

    s_l.sort()
    s_u.sort()
    s_n_odd.sort()
    s_n_even.sort()

    final = ''.join(s_l + s_u + s_n_odd + s_n_even)

    return print(final)

#ginortS('Sorting1234')



#import numpy as np
def athleteSort():
    """
    Solved this problem using numpy, but need to solve without numpy
    """

    sizes = input().split()
    n,m = int(sizes[0]), int(sizes[1])
    del sizes

    arr = np.empty((n, m))
    arr[:] = np.nan
    for i in range(n):
        col = input().split()
        col = [int(x) for x in col]
        arr[i, :] = col.copy()
        del col
    arr = arr.astype(int)

    k = int(input())         # column to sort on

    ind = arr[:,k].argsort() # get indices of sorted column k
    arr_sorted = arr[ind, :]

    for i in range(n):
        to_print = arr_sorted[i, :].copy()
        print(' '.join(map(str, to_print)))

    return

#athleteSort()

def athleteSort1():
    """
    Solved this problem using numpy, but need to solve without numpy
    """

    sizes = input().split()
    n,m = int(sizes[0]), int(sizes[1])
    del sizes

    # Collect nested list
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # Transpose a nested list
    arr_t = list(map(list, zip(*arr)))

    k = int(input())         # column to sort on

    # get indices of sorted column k
    ind = [i[0] for i in sorted(enumerate(arr_t[k]), key=lambda x: x[1])]

    # Re-order
    arr_n = []
    for ii in range(m):
        arr_n.append([arr_t[ii][i] for i in ind])

    # Transpose a nested list - final
    arr_f = list(map(list, zip(*arr_n)))

    for i in range(n):
        to_print = arr_f[i]
        print(' '.join(map(str, to_print)))

    return

#athleteSort1()


import numpy as np

def sumANDproduct():
    """
    https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
    """

    sizes = input().split()
    N, M = int(sizes[0]), int(sizes[1])

    arr = np.zeros((N, M))

    for i in range(N):
        input_row = [int(x) for x in input().split()]
        arr[i, :] = input_row.copy()

    sum_vector = np.sum(arr, axis=0)
    result = np.prod(sum_vector)

    return print(int(result))

# sumANDproduct()


