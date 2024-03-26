# KMP算法：解决字符串中最短重复单元问题
def compute_LPS_array(pattern):
    """计算部分匹配表（Longest Prefix Suffix）"""
    length = 0 # 当前最长的相等前后缀的长度
    lps = [0] * len(pattern) # *构建部分匹配表*
    i = 1 # 模式字符串的位置

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

def find_smallest_repeating_unit(s):
    """找到最小重复单元"""
    lps = compute_LPS_array(s)
    length = len(s)
    # 部分匹配表的最后一个值
    last_lps_value = lps[-1]
    if last_lps_value > 0 and length % (length - last_lps_value) == 0:
        return s[:length - last_lps_value]
    else:
        return s

# 示例
s = "abacabab"
print(find_smallest_repeating_unit(s))
print(compute_LPS_array(s))