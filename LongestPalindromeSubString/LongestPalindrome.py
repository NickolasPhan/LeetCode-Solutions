class Solution:
    def longestPalindrome(self, s: str) -> str:
        print("Evaluating:", s)
        index = 0

        for char in s:
            if s[index] == s[index+1]:
                pass

        # print(s[::-1])

def main():
    # s = "Hello World!"
    s = "babad"
    # s = input("Input test string:")
    solution = Solution()
    solution.longestPalindrome(s)

if __name__ == "__main__":
    print()
    main()
    print()