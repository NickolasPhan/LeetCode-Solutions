class Solution:
    def longestPalindrome(self, s: str) -> str:
        print("Evaluating:", s)
        testString = ""
        resStrings = []

        i = 0
        biggestStr = ""
        

        # it looks for two letters and evaluates whatever is between them
        while i < len(s):
            if i == 0 or i == len(s)-1:
                i += 1
                continue
            else:
                current = s[i]
                prev = s[i-1]
                next = s[i+1]

            if prev == next and (next-prev) > len(biggestStr):
                biggestStr = s[prev:next+1]
                print(biggestStr)

            i += 1

        return "End\n\n"

def main():
    # s = "Hello World!"
    # s = input("Input test string:")
    strings = ["sbababd", "cbbd", "a", "jfewjfewjjfwebookoobfjiewjfewjefw"]
    s = "sbababd"

    solution = Solution()
    for str in strings:
        print(solution.longestPalindrome(str))
    

if __name__ == "__main__":
    print()
    main()
    print()