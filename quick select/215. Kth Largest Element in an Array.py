'''
215. Kth Largest Element in an Array
https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            left = 0
            right = len(nums) - 1
            while left <= right:
                print(left, right, nums)
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
        ans = quick_select(nums, len(nums) - k)
        # print(nums)
        return ans
