class Solution:
    def longestPalindrome(self, s: str) -> str:
        print("Evaluating:", s)
        testString = ""
        resStrings = []
        i = 0
        j = 0

        # it looks for two letters and evaluates whatever is between them

        while i < len(s):
            j = i

            while j < len(s):
                testString += s[j]

                if testString == testString[::-1]:
                    resStrings.append(testString)

                j += 1
            testString = ""

            i += 1
        
        try:
            bigString = max(resStrings, key=len)
        except ValueError:
            return []
        else:
            return bigString

def main():
    # s = "Hello World!"
    s = input("Input test string:")
    solution = Solution()
    print(solution.longestPalindrome(s))

if __name__ == "__main__":
    print()
    main()
    print()