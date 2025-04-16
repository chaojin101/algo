'''
https://leetcode.cn/problems/top-k-frequent-elements/description/
'''

import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def quick_select(nums, k):
            left = 0
            right = len(nums) - 1
            while left <= right:
                pivot = nums[right]
                store_idx = left
                for i in range(left, right):
                    if nums[i] < pivot:
                        nums[i], nums[store_idx] = nums[store_idx], nums[i]
                        store_idx += 1
                nums[store_idx], nums[right] = nums[right], nums[store_idx]
                if k < store_idx:
                    right = store_idx - 1
                elif store_idx < k:
                    left = store_idx + 1
                else:
                    return nums[store_idx]

        counter = collections.Counter(nums)
        freqs = [(count, num) for num, count in counter.items()]
        n = len(freqs)
        k = n - k
        quick_select(freqs, k)
        
        ans = []
        for i in range(k, n):
            ans.append(freqs[i][1])
        return ans
