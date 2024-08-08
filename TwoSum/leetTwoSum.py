class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        solution = []

        for i, val in enumerate(nums):
            print(i, val, target)
            for j, jal in enumerate(nums):
                if i == j:
                    continue
                result = val + jal
                print(val, "+", jal, "=", result)
                if result == target:
                    solution.append(i)
                    solution.append(j)
                    return solution

result = Solution().twoSum(nums=[2, 7, 11, 15], target=9)
print(result, end="\n\n")

result = Solution().twoSum(nums=[3, 2, 4], target=6)
print(result, end="\n\n")

result = Solution().twoSum(nums=[3, 3,], target=6)
print(result, end="\n\n")

result = Solution().twoSum(nums=[-3, 4, 3, 90], target=0)
print(result, end="\n\n")
