class Solution:
    def intToRoman(self, num: int) -> str:
        if num > 3999 or num < 1:
            return -1

        integer_list = self.sepNumPlaces(num)
        #for num_el in integer_list:
        #    print('{:,}'.format(num_el))

        print(integer_list)

        romanDict = [['I', 'V'], ['X', 'L'], ['C', 'D'], ['M']]
        romanIndex = 0

        for value, power in integer_list:
            print("\n", value, sep="", end=" ")

            romanIndex = len(str(power))-1

            if value < 4:
                for i in range(1, value+1):
                    print(romanDict[romanIndex][0], end="")
            elif value < 9 and value != 4:
                print(romanDict[romanIndex][1], end="")
                for i in range(1, (value+1)%5):
                    print(romanDict[romanIndex][0], end="")

            else:
                if value == 4:
                    print(romanDict[romanIndex][0], end="")
                    print(romanDict[romanIndex][1], end="")
                    pass
                elif value == 9:
                    print(romanDict[romanIndex][0], end="")
                    print(romanDict[romanIndex+1][0], end="")
            
        print("\n\n==============================\n")

# ==========================================================================

    def sepNumPlaces(self, num: int) -> list:
        power = len(str(num)) - 1
        multi = 1 * 10**power
        res = []

        temp_num = num
        while(power >= 0):
            temp_power = temp_num//multi

            res.append((temp_power, multi))
            # res.append(temp_power*multi)
            temp_num = temp_num - temp_power*multi
            multi = 1 * 10**(power-1)

            power -= 1

        return res

print("\n============================================================\n")

Solution().intToRoman(num=1738)
Solution().intToRoman(num=9)
Solution().intToRoman(num=4)
Solution().intToRoman(num=90)
Solution().intToRoman(num=40)

print("\n============================================================\n")
