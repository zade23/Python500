# 问题：给定一个字符串（以字符数组的形式）和一个偏移量，根据偏移量原地从左向右旋转字符串
# 样例：给定 s = "abcdefg", offset = 3，返回 "efgabcd"

class Solution:
    def rotateString(self, s:list[str], offset:int):
        if len(s) > 0:
            offset = offset % len(s)
            temp = s[-offset:] + s[:-offset]
            for i in range(len(s)):
                s[i] = temp[i]
        

if __name__ == "__main__":
    s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    offset = 3
    solution = Solution()
    solution.rotateString(s, offset)
    print("输入：", s, "offset:", offset)
    print("输出：", s)