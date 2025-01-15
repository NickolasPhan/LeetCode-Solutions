class Solution():
    def checkPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = 's'
        i = 0
        for idx in range(len(s)):
            i = 0
            head, tail = idx, idx+1
            flag = True
            while True:
                if i == 0:
                    head = idx-i
                elif i == 1:
                    tail = idx+2
                else:
                    if i%2==0:
                        head -= 1
                    else:
                        tail += 1

                if head < 0 or tail > len(s):
                    break

                evalStr = s[head:tail]
                
                if self.checkPalindrome(s=evalStr):
                    if len(evalStr) >= len(longestPalindrome):
                        longestPalindrome = evalStr
                    flag = True
                    i += 1
                else:
                    if i > 1 and i%2==0:
                        if flag:
                            flag = not flag
                            i += 1
                            continue

                        flag = not flag
                        break
                    i += 1
                    continue
        
        return longestPalindrome

def main():
    var = Solution()

    strings = ["wvvvwqgjjgq", "tattarrattat", "sbababd", "cbbd", "aaaa", "jfewjfewjjfwebookoobfjiewjfewjefw"]

    for s in strings:
        print(f"\n\nStarting with {s}\n")
        print(var.longestPalindrome(s=s))

if __name__ == "__main__":
    print()
    main()
    print()