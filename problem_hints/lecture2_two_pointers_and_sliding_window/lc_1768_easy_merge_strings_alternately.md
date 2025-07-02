# 1768. Merge Strings Alternately

**Problem Link**: https://leetcode.com/problems/merge-strings-alternately/

## Easy approach (two pointers)
1. Use two pointers: i for word1, j for word2
2. While both pointers are within bounds, add characters alternately
3. Add remaining characters from the longer string
4. Return merged string

Time complexity: O(max(m, n)) - we iterate through the longer string
Space complexity: O(m + n) - we create new string


## Key insight
We need to merge two strings by taking characters alternately from each string. If one string is longer than the other, we append the remaining characters from the longer string. This is a straightforward string manipulation problem that can be solved with two pointers. 