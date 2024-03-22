# 问题：根据N名运动员的得分，找对相对等级（排名）。和获得最高分前三名的运动员，分别被分配金银铜牌。
# 其中N是正整数，并且不超过10000.所有运动员的乘积都保证是独一无二的。

class Solution:
    def findRelativeRanks(self, nums:list[int]) -> list[str]:
        score = {}
        for i in range(len(nums)):
            score[nums[i]] = i
        sortedScore = sorted(nums, reverse = True)
        answer = [0] * len(nums)
        for i in range(len(sortedScore)):
            res = str(i + 1)
            if i == 0:
                answer[score[nums[i]]] = "Gold Medal" # type: ignore
            elif i == 1:
                answer[score[nums[i]]] = "Silver Medal" # type: ignore
            elif i == 2:
                answer[score[nums[i]]] = "Bronze Medal" # type: ignore
            else:
                answer[score[nums[i]]] = res # type: ignore
        return answer # type: ignore

if __name__ == "__main__":
    solution = Solution()
    num = [5, 4, 3, 2, 1]
    ans = solution.findRelativeRanks(num)
    print("输入：", num)
    print("输出：", ans)