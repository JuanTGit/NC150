# Building with a stack

def reverseStr(string):
    stack = []
    res = ''
    for i in string:
        stack.append(i)
    while stack:
        res += stack.pop()

    return res

print(reverseStr('hello I am batman'))