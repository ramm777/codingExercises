# My solutions for the coderbyte.com challanges

def LongestWord(sen):

    """
    Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string.
    If there are two or more words that are the same length, return the first word from the string with that length.
    Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
    """

    pl = '!"#$%&()*+, -./:;<=>?@[\]^_`{|}~'

    words = sen.split()
    words1 = [w.strip(pl) for w in words]  # clean words

    lengths = ['' for x in range(0, len(words1))]
    for i in range(0, len(words1)):
        lengths[i] = len(words1[i])

    max_index = lengths.index(max(lengths))

    return words1[max_index]
    # return max(words1, key=len)

#print(LongestWord("fun&!! time007"))


def QuestionsMarks(strParam):

    """
    WARNING: This challange is questionable for the solution on Coderbyte.com
    Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters,
    and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
    If so, then your program should return the string true, otherwise it should return the string false. If there aren't any
    two numbers that add up to 10 in the string, then your program should return false as well. For example: if str is
    "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4,
     and 3 question marks between 5 and 5 at the end of the string.
    """

    for i in range(0, len(strParam)):

        if strParam[i].isnumeric():
            # print('num')
            newstring = strParam[i + 1:]
            for j in range(0, len(newstring)):
                if newstring[j].isnumeric():
                    # check if two numbers sums to 10
                    if int(strParam[i]) + int(newstring[j]) == 10:
                        focusedstring = newstring[:j]
                        # print(focusedstring)
                        questions = [x == '?' for x in focusedstring]
                        if sum(questions) >= 3:
                            return True
                        else:
                            continue
                    else:
                        continue

                else:
                    continue

        else:
            # print('nonnum')
            continue

    return False


#print(QuestionsMarks(input()))


def CodelandUsernameValidation(strParam):

    """
    Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

    1. The username is between 4 and 25 characters.
    2. It must start with a letter.
    3. It can only contain letters, numbers, and the underscore character.
    4. It cannot end with an underscore character.

    If the username is valid then your program should return the string true, otherwise return the string false.
    """

    if len(strParam) < 4 or len(strParam) > 25:
        return False

    if strParam[0].isalpha() == False:
        return False

    if strParam[-1] == '_':
        return False

    for i in strParam:
        if i.isalpha() == True or i.isnumeric() == True or i == '_':
            continue
        else:
            return False

    return True

#print(CodelandUsernameValidation(input()))


def BracketMatcher(strParam):

    """
    WARNING: my code doesn't work for double brackets e.g. "(hello (world))"
    Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly
    matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1,
    but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. Only "(" and ")" will
    be used as brackets. If str contains no brackets return 1.
    """

    if strParam.find('(') == -1 or strParam.find(')') == -1:
        return 1

    for i in range(len(strParam)):

        # check if opening is present
        if strParam[i] == '(':
            # check if closing is present
            newstring = strParam[i + 1:]
            for j in range(len(newstring)):
                if newstring[j] == ')' or newstring[j] == '(':
                    if newstring[j] == ')':
                        break
                    elif newstring[j] == '(':
                        return 0
                elif j == len(newstring) - 1:
                    return 0
                else:
                    continue

        elif strParam[i] == ')':
            newstring = strParam[:i]
            newstring = newstring[::-1]
            for j in range(len(newstring)):
                if newstring[j] == ')' or newstring[j] == '(':
                    if newstring[j] == '(':
                        break
                    elif newstring[j] == ')':
                        return 0
                elif j == len(newstring) - 1:
                    return 0
                else:
                    continue

        else:
            continue

    return 1


def BracketMatcher1(str):
    """
    Much more elegant code from example solutions on Coderbyte.com
    """

    count = 0
    for c in str:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0: return 0

    return 1 if count == 0 else 0

#print(BracketMatcher1("(hello (world))"))
#print(BracketMatcher("(hello (world))"))


import numpy as np
def arrayChallenge(arr):
    """
    This is PwC 1st exercise
    https://datascience.stackexchange.com/questions/93440/preparing-for-interview-logistic-regression-question
    I only don't understand why bias doesn't have X when updated.
    """
    learnrate = 1

    X = arr[0]
    y = arr[1]
    weights = arr[2]
    bias = arr[3]

    x_plot = range(-5, +5)
    y_plot = 1 / (1 + np.exp(np.dot(x_plot, -weights) - bias))

    plt.plot(x_plot, y_plot)
    plt.show()
    print("Note that the provided node [X,y] is outside the relationship")

    # Fix X, calculate y
    y_hat = 1 / (1 + np.exp(np.dot(X, -weights) - bias))
    plt.plot(X, y_hat, 'x')
    plt.show()

    # Fix y, calculate X. Cant' calculate it as can't divide by 0
    # x_hat = (-1/weights)*np.log((1-y)/y) - (bias/weights)

    new_weights = weights - learnrate * (y - y_hat) * X
    new_bias = bias - learnrate * (y - y_hat)

    return print("%.2f" % new_weights, "%.2f" % new_bias)

#arrayChallenge([2.2, 0, 5.1, 5.7])
#arrayChallenge([1, 1, 1, 1])

def movingMedian(arr_given):

    """
    Excercise: Array Challenge

    Have the function ArrayChallenge (arr) read the array of numbers stored in arr which will contain a sliding window size, N, as the first element in the array and the rest will be a list of numbers. Your program should return the Moving Median for each element based on the element and its N-1 predecessors, where N is the sliding window size. The final output should be a string with the moving median corresponding to each entry in the original array separated by commas.
    Note that for the first few elements (until the window size is reached), the median is computed on a smaller number of entries. For example: if arr is [3, 1, 3, 5, 10, 6, 4, 3, 1] then your program should output "1,2,3,5,6,6,4,3"
    Examples
    Input: [5, 2, 4, 6] Output: 2,3,4
    Input: [3, 0, 0, -2, 0, 2, 0, -2] Output: 0,0,0,0,0,0,0

    Aidan:
    Median formulas for python (index from 0):
        Odd length array:
            median = array[(((length+1)/2) - 1)]
        Even length array:
            median = array[ind_low_middle] + array[ind_up_middle]) / 2

    Be careful with the formulas on the internet, they may be misleading
    """

    arr = arr_given[1:]
    window = arr_given[0]
    del arr_given

    arr_result = []
    for i in range(len(arr)):
        ind_stop = i+1
        ind_start = i+1-window
        if ind_start < 0: ind_start = 0

        subarray = arr[ind_start : ind_stop]
        subarray.sort()
        length = len(subarray)

        if length%2 == 0: # even
            ind_low = int((length/2) - 1)
            ind_up = int(ind_low + 1)
            median = (subarray[ind_low] + subarray[ind_up]) / 2
        else:             # odd
            median = subarray[int(((length+1)/2) - 1)]
        arr_result.append(int(median))

    return print(arr_result)

#arr = [3, 1, 3, 5, 10, 6, 4, 3, 1]
#arr = [5, 2, 4, 6]
arr = [3, 0, 0, -2, 0, 2, 0, -2]
movingMedian(arr)


