# 问题：合并两个排序的整数数组A和B变成一个新的数组。
class Solution:
    # 双指针实现
    def mergeSortedArray(self, a:list[int], b:list[int]) -> list[int]:
        l, r = 0, 0
        result  = []
        while l < len(a) and r < len(b):
            if a[l] < b[r]:
                result.append(a[l])
                l += 1
            else:
                result.append(b[r])
                r += 1
        while l < len(a):
            result.append(a[l])
            l += 1
        while r < len(b):
            result.append(b[r])
            r += 1
        return result
    
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    solution = Solution()
    ans = solution.mergeSortedArray(a, b)
    print("输入：", a, b)
    print("输出：", ans)