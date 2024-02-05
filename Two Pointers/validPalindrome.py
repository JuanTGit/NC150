# 125. Valid Palindrome
# Easy
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
# all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters 
# include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
s = "3A man, a plan, a canal: Panama3"
def validPalindrome(s):
    l, r = 0, len(s) - 1

    while l <= r:
        if s[l].isalnum() and s[r].isalnum():
            if s[l].lower() != s[r].lower():
                return False
            else:
                r -= 1
                l += 1
        elif s[l].isalnum():
            r -= 1
        elif s[r].isalnum():
            l += 1
        else:
            l += 1
            r -= 1
    return True

print(validPalindrome(s))