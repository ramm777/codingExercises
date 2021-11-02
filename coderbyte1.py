
def commonElements(str1, str2):
    """
    Check which elements in list1 are present in list2
    """
    results = []
    for element in str1:
        if element in str2:
            results.append(element)
            str2.replace(element, '', 1)
    return results

def MinWindowSubstring(strArr):

  strN = strArr[0]
  strK = strArr[1]

  substrings_all = []
  for i in range(0,len(strN)):
    for j in range(len(strN),0,-1):

      substringN = strN[i:j]
      common = commonElements(strK, substringN)
      common1 = commonElements(substringN, strK)

      if len(common) >= len(strK) and len(common1) >= len(strK):
        substrings_all.append(substringN)

  return min(substrings_all, key=len)

#                              K                  N
#ex1 = ["ahffaksfajeeubsne", "jefaa"] # must be aksfaje
#ex2 = ["aabdccdbcacd", "aad"]
#ex3 = ["aaabaaddae", "aed"]
#ex4 = ["aaffhkksemckelloe", "fhea"]
#print(MinWindowSubstring(ex1))


class Solution:
    def reverse(self, x: int) -> int:

        x = str(x)

        if x[0] == '-':
            sign = -1
            x = x.replace('-', '', 1)
        else:
            sign = 1

        x = list(x)
        reversed_list = x[::-1].copy()
        reversed_str = ''.join(reversed_list)
        reversed_int = int(reversed_str)
        reversed_int = reversed_int * sign

        if reversed_int < -2 ** 31 or reversed_int > 2 ** 31 - 1:
            return 0

        return reversed_int

#Solution = Solution()
#print(Solution.reverse(0))

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        s = list(s)

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                s_temp = s.copy()
                s_temp[i], s_temp[j] = s_temp[j], s_temp[i]

                #print(''.join(s_temp))
                if ''.join(s_temp) == goal:
                    return True

        return False


#Solution = Solution()
#Solution.buddyStrings("aaaaaabc", "aaaaaacb")

class Solution:
    def longestCommonPrefix(self, strs) -> str:

        """
        Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
        Example 1:
        Input: strs = ["flower","flow","flight"]
        Output: "fl"
        """

        if len(strs) > 200 or len(strs) < 1: return ""
        for i in range(len(strs)):
            if len(strs[i]) > 200 or len(strs[i]) < 0: return ""

        items_num = len(strs)
        common_prefix = ""

        for j in range(len(strs[0])):

            trues = 0
            for i in range(items_num):
                try:
                    if strs[0][j] == strs[i][j]:
                        trues = trues + 1
                except: return common_prefix
            if trues == items_num:
                common_prefix = strs[0][0:j + 1]
            else:
                break

        return common_prefix


#Solution = Solution()
#print(Solution.longestCommonPrefix(["flower","flow","floight"]))

class Solution:
    def isValid(self, s: str) -> bool:

        residual = len(s) % 2
        if residual == 0:
            centre = int(len(s) / 2)
        else:
            return False

        nums = [0 for x in range(len(s))]
        for i in range(len(s)):
            if s[i] == "(": nums[i] = 1
            if s[i] == ")": nums[i] = -1
            if s[i] == "{": nums[i] = 20
            if s[i] == "}": nums[i] = -20
            if s[i] == "[": nums[i] = 10
            if s[i] == "]": nums[i] = -10

        if sum(nums) != 0: return False

        if nums[centre-1] + nums[centre] != 0:
            return False

        #for i, j in zip(range(centre, len(s) + 1), range(centre - 1, -1, -1)):
        #    if nums[i] + nums[j] != 0:
        #        return False
        #    else:
        #        continue

        return True

#string = "()[]{}"
#Solution = Solution()
#print(Solution.isValid(string))

#import statistics

#numbers =  [4,3,1]
#window_size = 3

#i = 0
#moving_averages = []
#while i < len(numbers) - window_size+1:
#    this_window = numbers[i : i + window_size]#
#
#    window_average = statistics.median(this_window)
#    moving_averages.append(window_average)
 #   i += 1
#print(moving_averages)







