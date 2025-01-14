class Solution():
    def checkPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = 's'
        i = 0
        for idx, char in enumerate(s):
            print("looking at:", char)

            # What do you want to do?
            # From a char in the string,
            # take it and starting from itself,
            # look at a string if it were that char
            # and the two characters ahead and behind it.
            # if it is a palindrome, keep expanding.
            # if it is longer than the current
            # 'longestPalindrome', keep going.
            # if it isn't, continue.
            # if it finishes but isn't longer than the longest palindrome, continue.


            # Now: Change it to instead of viewing a single letter, it is viewing the cursor
            i = 0
            head = idx-i
            tail = idx+i+1
            while True:
                if i % 2 == 0:
                    # head = idx-i
                    head = idx-i if i > 0 else idx
                else:
                    tail = idx+i+1

                if head < 0 or tail > len(s):
                    break

                evalStr = s[head:tail]
                
                if self.checkPalindrome(s=evalStr):
                    if len(evalStr) >= len(longestPalindrome):
                        longestPalindrome = evalStr
                        print(longestPalindrome)
                    i += 1
                else:
                    # i += 1
                    break

        return longestPalindrome

def main():
    var = Solution()

    strings = ["sbababd", "cbbd", "a", "jfewjfewjjfwebookoobfjiewjfewjefw"]
    # string = "babad"

    for s in strings:
        print(var.longestPalindrome(s=s))
    # test = var.longestPalindrome(s=string)
    
    # print(f'\n{test}')

if __name__ == "__main__":
    print()
    main()
    print()