# 242. Valid Anagram
# Easy
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

#     1 <= s.length, t.length <= 5 * 104
#     s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


def isValid(s, t):
	# Check is for edgecase that we iterate through len(s) and it's shorter then len(t)
	if len(s) != len(t): return False
	countS, countT = {}, {}
	# Iterate through the length of either and add each character into a hashmap
	for i in range(len(s)):
		countS[s[i]] = countS.get(s[i], 0) + 1
		countT[t[i]] = countT.get(t[i], 0) + 1
	# Return a boolean when comparing
	return countS == countT

# Leetcode Stopwatch: 00 : 01 : 58