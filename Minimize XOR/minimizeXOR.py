class Solution:
    def getNumBits(self, num: int) -> int:
        pass

    def minimizeXor(self, num1: int, num2: int) -> int:
        print(f'num1: {num1:0>{num2.bit_length()}b}\nnum2: {num2:b}\n')
        print(f'num1 bit length: {num1.bit_length()}\nnum2 bit length: {num2.bit_length()}\n')
        # print(f'dec: {xor}\nbit: {xor:b}\nbit count: {xor.bit_count()}')

        # naive solution : brute force

        # solutionBank = []

        # i = num1+1
        i = 0
        print(i)
        while True:
            if i.bit_count() != num2.bit_count():
                i += 1
                continue
            else:
                return i
                # i += 1


def main():
    var = Solution()
    
    num1 = 25
    num2 = 72

    res = var.minimizeXor(num1=num1, num2=num2)

    print(f'dec: {res}\nbin: {res:b}')

    print(f'\nresult: {res} XOR num1: {num1}\nXOR result: {res^num1}')

    # for num in res:
    #     print(f'{num:b}')

if __name__ == "__main__":
    print()
    main()
    print()