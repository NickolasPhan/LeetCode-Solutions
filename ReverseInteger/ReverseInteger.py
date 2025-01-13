class Solution:
    def reverse(self, n: int) -> int:
        flag = True if n < 0 else False
        n_str = str(abs(n))[::-1]
        if flag:
            n_str = '-' + n_str

        n_int = int(n_str)

        if -2**31 <= n_int <= 2**31 - 1:
            return int(n_str)
        else:
            return 0

def main():
    var = Solution()

    res = var.convert(n=-123)

    print(res)

if __name__ == "__main__":
    print()
    main()
    print()