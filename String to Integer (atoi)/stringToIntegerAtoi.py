class Solution:
    def myAtoi(self, s: str) -> int:
        res = ''
        s = s.strip()

        flag = False
        try:
            if s[0] == '-':
                flag = True
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]
        except IndexError:
            return 0

        for char in s:
            if char.isnumeric():
                res += char
            else:
                break

        res = int(res) if res else 0
        res = res*-1 if flag else res

        if -2**31 > res:
            res = -2**31
        elif res > 2**31 - 1:
            res = 2**31 - 1
        
        return res


def main():
    var = Solution()

    string = "   -042"

    res = var.myAtoi(s=string)
    print(res)

if __name__ == "__main__":
    print()
    main()
    print()