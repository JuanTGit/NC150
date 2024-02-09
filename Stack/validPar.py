# 20. Valid Parentheses
# Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false 

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
s = "())"
def validParentheses(s):
    # Hash table to map open brackets to closed brackets.
    bracket = { '(':')', '[':']', '{':'}' }
    # Stack to add open brackets and compare closing ones in order.
    stack = []

    for i in s:
        if i in bracket:
            stack.append(i)
        elif len(stack) > 0 and bracket[stack.pop()] == i:
            continue
        else:
            return False

    return stack == []

print(validParentheses(s))