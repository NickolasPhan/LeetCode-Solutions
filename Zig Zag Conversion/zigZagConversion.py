class Solution:
    def convert(self, s: str, numRows: int) -> str:
        print(s)

        all_list = []
        curr_list = []
        initArr = ['' for i in range(numRows)]
        numZags = numRows - 2
        # working on - how to know when the loop is in the zag section? how to navigate that?

        for idx, char in enumerate(s):
            curr_list.append(char)

            if (idx+1)%numRows==0:
                all_list.append(curr_list)
                curr_list = []

        print(initArr)

def main():
    var = Solution()

    string = 'PAYPALISHIRING'
    rows = 3

    var.convert(string, rows)

if __name__ == "__main__":
    print()
    main()
    print()