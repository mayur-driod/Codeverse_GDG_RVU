# 2 Sum Problem (Easy) - Arrays
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# 3 Sum Problem (Easy) - Arrays
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums)-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k-=1
                elif total < 0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1

                    while nums[j] == nums[j-1] and j<k:
                        j+=1
        return res

# Longest Consecutive  Sequence (Medium) - Arrays 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Nset = set(nums)
        lng = 0

        for n in Nset:
            if n - 1 not in Nset:
                length = 1

                while n + length in Nset:
                    length += 1
                
                lng = max(lng, length)
        
        return lng

# Merge Intervals (Hard) - Arrays*
class Solution:
    def merge(self, intervals):
        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = result[-1][1]
            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])

        return result
# Roman to Integer (Medium) - Strings
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result

# String to Integer (Hard) - Strings
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0

        x, i, r = 1, 0, 0
        if s[0] == '-':
            x = -1
            i += 1
        elif s[0] == '+':
            i += 1
        while i < len(s) and s[i].isdigit():
            r = r * 10 + int(s[i])
            if x * r > 2**31 - 1:
                return 2**31 - 1
            if x * r < -2**31:
                return -2**31
            i += 1
        return x * r

# Largest Rectangle in Histogram (Hard) - 
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        stack = []
        max_area = 0

        for i,height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h,j = stack.pop()
                w = i-j
                a = h*w
                max_area = max(max_area,a)
                start = j
            stack.append((height,start))
        
        while stack:
            h,j = stack.pop()
            w = n-j
            max_area = max(max_area,h*w)
        return max_area
