strs = ['flower', 'flow', 'flight']

def longestCommonPrefix(strs):
    res = ""

    for i in range(len(strs[0])):
        for str in range(len(strs)):
            if i == len(strs[str]) or strs[0][i] != strs[str][i]:
                return res
        res += strs[0][i]
    return res


print(longestCommonPrefix(strs))


def testLoop(strs):

    for i in range(len(strs)):
        print(i)

# print(testLoop(strs))