'''
https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/
'''

'''
1. naive dfs
2. dfs pruning (https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solutions/1441006/by-lfool-d9o7/)
'''

# 1. naive dfs
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        size = total // k

        buckets = [0] * k
        def dfs(i):
            if i < 0:
                if all(bucket == size for bucket in buckets):
                    return True
                return False
            for j in range(k):
                buckets[j] += nums[i]
                if dfs(i - 1):
                    return True
                buckets[j] -= nums[i]
            return False
        return dfs(len(nums) - 1)

# 2. dfs pruning (https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solutions/1441006/by-lfool-d9o7/)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        size = total // k

        nums.sort()

        buckets = [0] * k
        def dfs(i):
            if i < 0:
                return True
            for j in range(k):
                if j > 0 and buckets[j] == buckets[j - 1]:
                    continue
                buckets[j] += nums[i]
                if buckets[j] <= size and dfs(i - 1):
                    return True
                buckets[j] -= nums[i]
            return False
        return dfs(len(nums) - 1)
