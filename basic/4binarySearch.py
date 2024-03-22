# 问题：给定一个排序的整数数组（升序）和一个要查找的目标整数target，
# 用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。

class Solution:
    def binarySearch(self, nums:list[int], target:int) -> int:
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + end >> 1
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid 
        return start

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 3, 4, 5, 10]
    target = 3
    ans = solution.binarySearch(nums, target)
    print("输入：", nums, "目标：",target)
    print("输出：", ans)
