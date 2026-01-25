# Fixed length Sliding Window - Leetcode 643

from typing import List


class solution:
    def findMaxAverage(self, nums: List[int], k:int) -> float:
        n = len(nums)
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[i]
        
        max_sum = cur_sum / k

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]

            avg = cur_sum / k
            max_sum = max(max_sum, avg)

        return max_sum

print(solution().findMaxAverage([1,12,-5,-6,50,3], 4))

# time : O(n)
# space : O(1)