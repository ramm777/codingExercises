# https://www.hackerrank.com/challenges/

def isLeapYear(year):
    if year <= 1900 or year >= 10**5: return False
    isleap = False

    if year%4 == 0:
        isleap = True
        if year%100 == 0:
            isleap = False
            if year%400 == 0:
               isleap = True

    return isleap

def isLeapYear1(year):
    return year%4==0 and (year%400 == 0 or year%100 !=0)

#print(isLeapYear(1992))

def someFunction0(n):
    assert type(n) == int
    assert n >= 1 and n <= 100

    if n%2 != 0: print("Weird")
    else:
        if n >= 2 and n <=5: print("Not Weird")
        if n >= 6 and n <=20: print("Weird")
        if n > 20: print("Not Weird")

def someFunction1(n):
    """
    Hint: abstract it. Loom at Not weird first that includes odd/even, then or comes within.
    """

    check = {True: "Not Weird", False: "Weird"}
    print(check[ n % 2 == 0 and (n in range(2, 6) or n > 20)  ])

# someFunction1(6)

def count_substring(string, sub_string):

    num = 0
    lens = len(sub_string)
    for i in range(len(string)):
        nstring = string[i : lens+i]
        #print(nstring)
        if nstring == sub_string:
            num = num+1

    return num

#print(count_substring("ABCDCDC", "CDC"))

def findRunnerupScore(n, arr):
    arr = list(arr)
    arr.sort()
    #print('Sorted array: %s' % arr)

    i = 1
    while arr[-1-i] == arr[-1]:
        #print(arr[-1-i])
        item = arr[-1-i]
        i = i + 1;

    return arr[-1-i]

#n = 5
#arr = [2,3,6,10,5,8, 10, 10]
#print('Results: %s' % findRunnerupScore(n, arr))

def showSecondLowestGrade(nest_list): # in a nested list
    # Sort a nested list based on the score x[1]
    list_all = nest_list.copy()
    list_all.sort(key=lambda x: x[1])

    print("Sorted list all: %s" % list_all)

    # If the are more than one minimum scores, find the last one in a list
    ind = 0
    for i in range(0, len(list_all)):
        if list_all[ind+1][1] == list_all[ind][1]:
            ind = ind + 1

    # Runner-up single
    ind_r = ind + 1
    result_names = [list_all[ind_r][0]]

    # If the are more than one runner-up minimum score
    for i in range(ind_r, len(list_all) - ind_r):
        if list_all[i][1] == list_all[i + 1][1]:
            result_names.append(list_all[i + 1][0])
        else: break

    result_names.sort()

    for i in range(len(result_names)):
        print(result_names[i])

# Check this is wrong answer for some reason. Must be Beria Harsh
#nest_list = [["Harsh", 20], ["Beria", 20], ["Varun", 19], ["Kakunami", 19], ["Vikas", 21]]
#nest_list = [["Sona", -25.001], ["Mona", -25.0001], ["Mini", -25.000], ["Rita", -25.0]]
#showSecondLowestGrade(nest_list)


def swap_case(s):

    ns = ""
    for item in s:
        if item.islower():
            ns = ns + item.upper()
        else:
            ns = ns + item.lower()

    return ns

# print(swap_case('HackerRank.com presents "Pythonist 2".'))


def permutations0(s, k):
    """
    Warning: this works only for the k = 2. For k > 2 it is more difficult problem I decided not to solve (re-inveting a wheel)
    """
    list1 = []
    for item1 in s:
        for item2 in s:
            if item1 != item2:
                perm = item1 + item2
                list1.append(perm)
            else:
                continue
    return print(list1)


#from itertools import permutations
def permutations1(s, k):
    list1 = list(s)
    list1.sort()
    perms = list(permutations(list1, k))

    list2 = []
    for i in range(len(perms)):
        list2.append(''.join(perms[i]))

    for item in list2:
        print(item)

    return

#print("Please type in your input here, for example: HACK 2")
#inputs = input()
#inputs = inputs.split(' ')
#s = str(inputs[0])
#k = int(inputs[1])
#permutations1(s, k)


#from itertools import combinations
def combinations0(s, k):
    list1 = list(s)
    list1.sort()

    combs = [] # nested list
    for ks in range(1, k + 1):
        combs.append(list(combinations(list1, ks)))
    del ks

    list2 = []
    for ks in range(len(combs)):
        for i in range(len(combs[ks])):
            list2.append(''.join(combs[ks][i]))


    for item in list2:
        print(item)

    return

#print("Please type in your input here, for example: HACK 2")
#inputs = input()
#inputs = inputs.split(' ')
#s = inputs[0]
#k = int(inputs[1])
#combinations0(s, k)



#import numpy as np
#n = int(input())
#print('Provide the 1st matrix using space between the entries')
#a = np.array([input().split() for _ in range(n)],int)
#print('Provide the 2nd matrix')
#b = np.array([input().split() for _ in range(n)],int)
#reults = np.dot(a, b)


def findPercentage(student_marks, query_name):

    marks = student_marks[query_name]
    average = sum(marks) / len(marks)

    return print('%.2f' % average)

#print('Input data manually: ')
#n = int(input())
#student_marks = {}
#for _ in range(n):
#    name, *line = input().split()
#    scores = list(map(float, line))
#    student_marks[name] = scores
#query_name = input()
#print(student_marks)
#findPercentage(student_marks, query_name)

def lists_actions(command, list1):
    todo = command.split(' ')
    del command

    # Split to parameters
    command = todo[0]
    if len(todo) == 2:
        e = int(todo[1])
    elif len(todo) == 3:
        e = int(todo[2])
        ind = int(todo[1])
    del todo

    # Actions
    if str(command) == 'append': list1.append(e)
    if str(command) == 'insert': list1.insert(ind, e)
    if str(command) == 'print': print(list1)
    if str(command) == 'remove': list1.remove(e)
    if str(command) == 'sort': list1.sort()
    if str(command) == 'reverse': list1.reverse()
    if str(command) == 'pop': list1.pop()

    #print(list1)
    return list1


#n = int(input()) # number of commands
#list1 = []
#for i in range(n):
#    command = input()
#    list1 = lists_actions(command, list1)


def hashTuple(n, integer_list):

    print(integer_list)
    tuple1 = tuple(integer_list)
    t = hash(tuple1)

    return print(t)

#n = int(input())
#integer_list = list(map(int, input().split()))
#hashTuple(n, integer_list)

def wrap(string, max_width):
    assert max_width > 0

    num = int(len(string) / max_width)
    residual = len(string) - num * max_width

    n_string = ''
    for i in range(0, num * max_width, max_width):
        #print(string[i: i + max_width])
        n_string = n_string + string[i: i + max_width]
        n_string = n_string + '\n'

    #print(string[num * max_width:])
    n_string = n_string + string[num * max_width:]

    return n_string


#if __name__ == '__main__':
#    string, max_width = input(), int(input())
#    result = wrap(string, max_width)
#    print(result)


# Complete the solve function below.
def solve(s):

    list1 = s.split(' ')
    print(list1)

    list_n = []
    for i in range(len(list1)):
        string = str(list1[i])
        if string == '':
            list_n.append(string)
        else:
            string_n = string[0].upper() + string[1:]
            list_n.append(string_n)
        del string

    return " ".join(list_n)

#s = " chris   alan  murhu well 12abc "
#s = "  hello   world  lol 012bb"
#print(solve(s))


def polyndromTriangle(size):
    for i in range(size):
        if i == 0: continue
        print( int(((10**i - 1) / 9)**2) )
    return

#polyndromTriangle(5)

#-------------------------------------------------------------------
# Re-shape numpy array
#import numpy
#n = '1 2 3 4 5 6 7 8 9'.split()
#list1 = [int(n[i]) for i in range(len(n))]
#arr = numpy.array(list1)
#arr1 = numpy.reshape(arr, (3,3))
#print(arr1)

#-------------------------------------------------------------------
# Numpy transpose, flatten
#import numpy as np
#
#inputs = input().split()
#N = int(inputs[0])
#M = int(inputs[1])
#
#arr = np.zeros((N,M), dtype=int)
#for i in range(N):
#    list1 = input().split()
#    list2 = [int(list1[x]) for x in range(len(list1))]
#    arr[i, :] = list2

#print(np.transpose(arr))
#print(arr.flatten())


#-------------------------------------------------------------------
#import numpy as np
#
#N, M, P = input().split()
#N = int(N)
#M = int(M)
#P = int(P)
#
#arr1 = np.zeros((N, P), dtype=int)
#arr2 = np.zeros((M, P), dtype=int)
#
#for i in range(N):
#    list1 = input().split()
#    list2 = [int(list1[x]) for x in range(P)]
#    arr1[i, :] = list2
#    del list1, list2
#
#for i in range(M):
#    list1 = input().split()
#    list2 = [int(list1[x]) for x in range(P)]
#    arr2[i, :] = list2
#    del list1, list2
#
#print(np.concatenate((arr1, arr2), axis=0))

#-------------------------------------------------------------------
#
#from collections import Counter

def companyLogo(s):

    """
    Come back here
    """

    s= sorted(s)

    list1 = [s[i] for i in range(len(s))]
    dic = dict(Counter(list1))

    key_list = list(dic.keys())
    val_list = list(dic.values())

    ind = [i[0] for i in sorted(enumerate(val_list), key=lambda x:x[1], reverse=True)]

    vals = []
    keys = []
    for i in range(3):
        vals.append(val_list[ind.index(i)])
        keys.append(key_list[ind.index(i)])

    print(str(keys))
    print(str(vals))
#s = 'bbbaaaccde'
#companyLogo(s)

#-------------------------------------------------------------------
#
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

#n = int(input())
#words = input().split()
#print(score_words(words))

#--------------------------------------------------------------------
# Errors and exceptions

def errorException(num):

    a_s = []
    b_s = []
    for i in range(num):
        inputs = input().split()
        a, b = inputs[0], inputs[1]
        a_s.append(a)
        b_s.append(b)
        del a, b

    for i in range(num):
        try:
            answer = int(a_s[i]) / int(b_s[i])
            print(int(answer))
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
        except ValueError as f:
            print("Error Code:", f)

    return

#num = int(input())
#errorException(num)


def numberIsPowerOfTwo(num):
    """
    Interview question => Check if the input integer num is a power of two.
    The alternative is to use log2(num) > https://www.geeksforgeeks.org/python-program-to-find-whether-a-no-is-power-of-two/
    """

    if num == 0: return print(False)
    if num < 0: return print(False)

    while num > 0:
        if num == float(1): return print(True)
        if num%2 != 0: return print(False)
        num = num/2

    return

#num = int(input())
#numberIsPowerOfTwo(num)

def listComprehensions(x,y,z,n):

    lists = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

    sums = [sum(lists[xx]) for xx in range(len(lists))]

    nlists = [lists[i] for i in range(len(lists)) if sums[i] != n]

    return print(nlists)

#x = 2
#y = 2
#z = 2
#n = 2
#listComprehensions(x,y,z, n)


