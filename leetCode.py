# Most interesting functions from the leetCode to remember


# https://leetcode.com/problems/roman-to-integer/
def romanToInt(s):
    '''
        This code is better than the one below. Rule => observe your information from large picture
        Draw schematics on a paper before attempting
        Notcie:
            if:
                I (1) < V (5)   X (10) => then subtracting
                X (10) < L (50) C (100) => then subtracting
                ...
            else:
                then adding

    '''

    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    summ = 0
    num = 0
    i = 0
    while i <= len(s)-1:
        if  i < len(s)-1 and dic[s[i]] < dic[s[i+1]]:
           num = dic[s[i+1]] - dic[s[i]]
           i=i+2
        else:
           num =  dic[s[i]]
           i=i+1
        summ = summ + num

    return  print("Answer: %s" % summ)

#romanToInt("DLXXII")

def romanToInt1(s):
    " Brut force approach"
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    summ = 0
    num = 0
    i = 0
    while i <= len(s)-1:

        # Check for special cases
        if i < len(s)-1 and s[i] == 'I':
            if s[i+1] == 'V':
                num = dic[s[i+1]] - dic[s[i]]
                i=i+1
            elif s[i+1] == 'X':
                num = dic[s[i+1]] - dic[s[i]]
                i=i+1
            else:
                num = dic[s[i]]
            summ = summ + num
            i=i+1
        elif i < len(s)-1 and s[i] == 'X':
                if s[i+1] == 'L':
                    num = dic[s[i+1]] - dic[s[i]]
                    i=i+1
                elif s[i+1] == 'C':
                    num = dic[s[i+1]] - dic[s[i]]
                    i=i+1
                else:
                    num = dic[s[i]]
                summ = summ + num
                i=i+1
        elif i < len(s)-1 and s[i] == 'C':
                if s[i+1] == 'D':
                    num = dic[s[i+1]] - dic[s[i]]
                    i=i+1
                elif s[i+1] == 'M':
                    num = dic[s[i+1]] - dic[s[i]]
                    i=i+1
                else:
                    num = dic[s[i]]
                summ = summ + num
                i=i+1

        # If it is not a special case, then it is a general case
        else:
            summ = summ + dic[s[i]]
            i=i+1
    return print("Answer: %s" % summ)
#romanToInt1('DCCX')

#-----------------------------------------------------------------------------------------------------------------------


