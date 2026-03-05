class Solution:
    def minOperations(self, s: str) -> int:
        l = len(s)

        arr1 = list(s)
        arr2 = list(s)

        count1 = 0
        count2 = 0

        for i in range(l):
            expected = '0' if i % 2 == 0 else '1'

            if arr1[i] != expected:
                count1 += 1
                arr1[i] = expected

        for i in range(l):
            expected = '1' if i % 2 == 0 else '0'

            if arr2[i] != expected:
                count2 += 1
                arr2[i] = expected

        return min(count1, count2)