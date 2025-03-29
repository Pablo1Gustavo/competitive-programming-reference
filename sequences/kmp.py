"""
Description: Knuth-Morris-Pratt algorithm for pattern matching.
Time complexity: O(n + m)
Space complexity: O(m)
"""

# Get the longest proper prefix which is also a suffix of the string.
def lps(s: str) -> list[int]:
    lps = [0] * len(s)
    index = 1
    length = 0
    while index < len(s):
        if s[index] == s[length]:
            length += 1
            lps[index] = length
            index += 1
        else:
            if length == 0:
                lps[index] = 0
                index += 1
            else:
                length = lps[length - 1]
    return lps


# Find all occurrences of the pattern in the text.
def kmp(text: str, pattern: str) -> list[int]:
    lps_table = lps(pattern)
    result = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                result.append(i - j)
                j = lps_table[j - 1]
        else:
            if j == 0:
                i += 1
            else:
                j = lps_table[j - 1]
    return result
    
