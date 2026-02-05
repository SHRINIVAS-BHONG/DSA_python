class solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest_num = nums[0]
        for num in nums:
            if abs(num) < abs(closest_num) or (abs(num) == abs(closest_num) and num > closest_num):
                closest_num = num
            else:
                return closest_num
            
    # Time Complexity: O(n)
    # Space Complexity: O(1)