# KMP算法：解决字符串的最长重复单元问题
def compute_LPS_array(pattern):
    """计算部分匹配表（Longest Prefix Suffix）"""
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def find_longest_repeating_unit(s):
    """找到最长重复单元"""
    lps = compute_LPS_array(s)
    length = len(s)
    # 寻找最长的满足条件的lps值
    for i in range(len(lps)-1, -1, -1):
        if lps[i] > 0 and length % (length - lps[i]) == 0:
            return s[:length - lps[i]]
    return s # 如果没有找到，则整个字符串是最长重复单元

# 示例
s = "abababab"
print(find_longest_repeating_unit(s))
