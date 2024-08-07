nums = [2, 4, 7, 11, 15]
nums_len = len(nums)

print(nums)
# target = int(input("Enter a sum: "))
target = 9 

print("Target:", target, "\n")

solution = []

for i in range(nums_len):
    if nums[i] > target:
        continue
    for j in range(nums_len):
        if nums[j] > target:
            continue
        result = nums[i]+nums[j]
        print(nums[i], "+", nums[j], "=", result)
        if result == target:
            solution.append(nums[i])
            solution.append(nums[j])
            break
    else:
        continue
    break

print(solution)
