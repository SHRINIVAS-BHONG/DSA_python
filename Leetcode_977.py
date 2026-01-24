# question number 977 - square of a sorted array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1
        result.reverse()
        return result
    
# Time complexity: O(n)
# Space complexity: O(n)
    