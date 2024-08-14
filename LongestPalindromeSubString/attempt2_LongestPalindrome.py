class Solution:
    def longestPalindrome(self, s: str) -> str:
        # print("Evaluating:", s)
        testString = ""
        duplicates = []
        resStrings = []

        # it looks for two letters and evaluates whatever is between them

        for char in s:
            if char in testString and len(testString) >= 1:
                if char not in duplicates:
                    duplicates.append(char)            
            testString += char
        
        # if len(s) != 0 and len(duplicates) == 0:
        #     return s[0]

        for dupChar in duplicates:
            # indices = [i for i, x in enumerate(duplicates) if x == dupChar]
            indices = [i for i, x in enumerate(s) if x == dupChar]

            # print(indices)
            
            for index in indices:
                # i = 0
                i = len(indices)-1
                # while i < len(indices):
                while i > 0:
                    if indices[i] > index or (duplicates.index(dupChar) == 0 and indices.index(index)==0):
                    # if indices[i] > index:
                        # print(index, dupChar, indices[i])

                        start = index if index > 0 else None
                        end = indices[i] if indices[i] > 0 else None

                        # slice excludes stop val
                        if end is not None:
                            normStr = s[start:end+1]
                        else:
                            normStr = s[start:end]
                        

                        if start is not None:
                            revStr = s[end:start-1:-1]
                        else:
                            revStr = s[end:start:-1]

                        if normStr == revStr:
                            # print(normStr)
                            resStrings.append(normStr)
                            # break
                    i -= 1
                # else:
                #     continue
                # break

        # return s[0]
        try:
            bigString = max(resStrings, key=len)
        except ValueError:
            return s[0]
        else:
            return bigString


def main():
    # s = "Hello World!"
    # s = input("Input test string:")
    # s = "sbabad"
    # s = "idibidi"
    # s = "abcba"
    # s = "abas"
    s = "aacabdkacaa"

    # print(s[1:0:-1])
    
    solution = Solution()
    print("Output:",solution.longestPalindrome(s))

if __name__ == "__main__":
    print()
    main()
    print()
