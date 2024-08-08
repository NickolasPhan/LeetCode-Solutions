class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        testStr = ''
        uniStr = ''
        index = 0

        for char in s:

            if s[index] not in testStr:
                testStr += char
            else:
                if len(testStr) > len(uniStr):
                    uniStr = testStr

            index += 1

        if len(testStr) > len(uniStr):
            uniStr = testStr

        print(uniStr, len(uniStr))

print()
print("Continuing case 6:")
Solution().lengthOfLongestSubstring(s="dvdf")
print("Case 1: abcabcbb")
Solution().lengthOfLongestSubstring(s="abcabcbb")
print()
