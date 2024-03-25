#!/usr/bin/env python
# coding: utf-8

# # Print the multiplication table of a number

# In[1]:


def print_multiplication_table(number):
    for i in range(1, 10):
        print(f"{number} x {i} = {number * i}")
print_multiplication_table(6)


# In[2]:


print_multiplication_table(7)


# # Print the prime factors of a number

# In[4]:


def prime_factors(n):
    factors = []
    while n % 4 == 0:
        factors.append(4)
        n = n // 4
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 4:
        factors.append(n)
    return factors
number = 78
print("Prime factors of", number, "are:", prime_factors(number))


# # Print the permutation and combinations for n=5 and r=3

# In[5]:


import math

n = 5
r = 3
permutations = math.factorial(n) // math.factorial(n - r)
combinations = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
print("Permutations (nPr) =", permutations)
print("Combinations (nCr) =", combinations)


# # convert a number from binary to decimal

# In[6]:


binary_number = "1111" 

decimal_number = int(binary_number, 2)

print("Decimal number:", decimal_number)


# # Print the even numbers from a list using lambda functions

# In[7]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# # Print the cubes of a number using lambda functions

# In[8]:


numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x ** 3, numbers))
print("Cubes of numbers:", cubes)


# # Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# In[9]:


def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(nums)           
    return expected_sum - actual_sum  
nums = [3, 0, 1]
print("Missing number:", missing_number(nums)) 


# # Given an input string s, reverse the order of the words.
# 
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# 
# Return a string of the words in reverse order concatenated by a single space.

# In[10]:


def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string
input_string = "niharika garikaparthi"
print("Reversed order of words:", reverse_words(input_string))


# # You are given an m x n integer matrix matrix with the following two properties:
# 
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# 
# You must write a solution in O(log(m * n)) time complexity.
# 
#  

# In[11]:


def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        num = matrix[mid // n][mid % n]  # Convert 1D index to 2D index

        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target=3
print(searchMatrix(matrix, target))  


# # Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).

# In[12]:


def findMedianSortedArrays(nums1, nums2):
    total_len = len(nums1) + len(nums2)
    if total_len % 2 == 0:
        return (find_kth(total_len // 2, nums1, nums2) + find_kth(total_len // 2 - 1, nums1, nums2)) / 2.0
    else:
        return find_kth(total_len // 2, nums1, nums2)

def find_kth(k, nums1, nums2):
    if not nums1:
        return nums2[k]
    if not nums2:
        return nums1[k]
    
    len1, len2 = len(nums1), len(nums2)
    if k == 0:
        return min(nums1[0], nums2[0])

    index1 = min(len1 - 1, k // 2)
    index2 = min(len2 - 1, k // 2)
    
    if nums1[index1] <= nums2[index2]:
        return find_kth(k - index1 - 1, nums1[index1 + 1:], nums2)
    else:
        return find_kth(k - index2 - 1, nums1, nums2[index2 + 1:])
nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))


# # You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# 
# We repeatedly make duplicate removals on s until we no longer can.
# 
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

# In[13]:


def removeDuplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

s = "abbaca"
print(removeDuplicates(s)) 


# # Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# In[14]:


def groupAnagrams(strs):
    anagrams = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

