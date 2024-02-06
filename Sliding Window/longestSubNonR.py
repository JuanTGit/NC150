# 3. Longest Substring Without Repeating Characters
# Medium
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

def lengthOfLongestSubstring(s):
    res = 0
    l = 0
    r = 0
    uniques = set()

    while r < len(s):
        while s[r] in uniques:
            uniques.remove(s[l])
            l += 1
        uniques.add(s[r])
        r += 1
        res = max(res, r - l)
    
    return res

print(lengthOfLongestSubstring('bbbbb'))