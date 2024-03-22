# 问题：给定一个三位数，将其各位数字反向输出
class Solution:
    def reverseInterger(self, number:int ):
        high = number  // 100
        number %= 100
        mid = number // 10
        low = number % 10
        return low * 100 + mid * 10 + high
    
if __name__ == "__main__":
    number = 123
    solution = Solution()
    ans = solution.reverseInterger(number)
    print("输入：", number)
    print("输出：", ans)