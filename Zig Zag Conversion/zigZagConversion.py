class Solution:
    def convert(self, s: str, numRows: int) -> str:
        all_list = []
        curr_list = []
        initArr = ['' for i in range(numRows)]
        numZags = numRows - 2
        zagFlag = False
        positionCounter = 0

        for char in s:
            if zagFlag and numZags != 0:
                zagArr = initArr[:]

                if numZags < 0:
                    zagArr[0] = char
                else:
                    zagArr[numZags] = char
                    
                all_list.append(zagArr)
                numZags -= 1

                if numZags == 0:
                    zagFlag = not zagFlag
                    numZags = numRows-2

                continue
            else:
                curr_list.append(char)
                positionCounter += 1

            if positionCounter%numRows==0:
                all_list.append(curr_list)
                curr_list = []
                zagFlag = not zagFlag
        else:
            if curr_list:
                if len(curr_list) != numRows:
                    curr_list.extend([""] * (numRows - len(curr_list)))
                all_list.append(curr_list)

        # print(all_list)

        result = self.createZigZag(lst=all_list, numRows=numRows)
        return result

    def createZigZag(self, lst: list, numRows: int) -> str:
        orderedLst = []
        for idx in range(numRows):
            chars = [sublist[idx] for sublist in lst if sublist]
            orderedLst += chars

        resultLst = [char for char in orderedLst if char]
        resultStr = ''.join(resultLst)

        return resultStr

def main():
    var = Solution()

    string = 'hinmicwsqhptvaprhlmdnjewwpvidxcmfpyqtxklebfzdwskhgnwrtvnksvorzczrbrmybyeeffhdarmggiaafnkxlapkdodgfqgiommvrtytmkauuauaphzajoloeoujgarwmfrgarzmdbjydfatmztyqgmuxjedlxcaftgflhuqldooiqjxqfvinjcksgqeguglnosavorgrhxcaizsnwabfcnalfgrzmepaypxniegsdisljkzhkcpmprxxxqwjwllxdiklosdrdxfohgwringzefwbytmwgxtjhdxwycpbawphcnbmajmeokhoftlmsexakuyixplxmagoojdospvjbcxhwivqpsqbpqjogwnswtimdlbxcwgeaenwoknde'
    rows = 40
    # string = 'PAYPALISHIRING'
    # rows = 3

    result = var.convert(string, rows)

    print(result)

if __name__ == "__main__":
    print()
    main()
    print()