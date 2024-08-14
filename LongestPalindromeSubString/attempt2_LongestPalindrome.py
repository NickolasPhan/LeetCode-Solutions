class Solution:
    def longestPalindrome(self, s: str) -> str:
        print("Evaluating:", s)
        testString = ""
        duplicates = []
        i = 0

        # print(s[1:])
        # print(s[2:].index("b"))

        # print(indices)

        # it looks for two letters and evaluates whatever is between them

        for char in s:
            if char in testString and len(testString) > 1:
                if char not in duplicates:
                    duplicates.append(char)
            
            testString += char

        for dupChar in duplicates:
            # indices = [i for i, x in enumerate(duplicates) if x == dupChar]
            indices = [i for i, x in enumerate(s) if x == dupChar]
            
            print(indices)
            print(dupChar)
            for index in indices:
                
                pass
        
        print(duplicates)
        print(testString)

def main():
    # s = "Hello World!"
    # s = input("Input test string:")
    s = "sbabad"
    solution = Solution()
    solution.longestPalindrome(s)

if __name__ == "__main__":
    print()
    main()
    print()
