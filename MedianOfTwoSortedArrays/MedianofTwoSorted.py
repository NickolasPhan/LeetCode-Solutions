import random

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:        
        # for x in nums2:
        #     nums1.append(x)

        # nums = nums1 + nums2

        # nums = [*nums1, *nums2]

        nums = nums1

        nums[0:0] = nums2
        
        nums.sort()

        midIndex = len(nums)/2

        if len(nums) % 2 == 0:
            left = midIndex -1
            return float((nums[int(midIndex)] + nums[int(left)])/2)
        else:
            return float(nums[int(midIndex)])

def main():
    print("Hello World!")
    arr1 = [random.randint(1,9) for x in range(random.randint(1,9))]
    arr2 = [random.randint(1,9) for x in range(random.randint(1,9))]

    # print(arr1)
    # print(arr2)

    solution = Solution()
    print("The solution:", solution.findMedianSortedArrays([], [2,3]))
    

if __name__ == "__main__":
    print("====================")
    main()
    print("====================")