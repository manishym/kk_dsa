# 14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix

## Easy approach (Character by character comparison)
1. If array is empty, return empty string
2. Take first string as the initial prefix
3. For each other string in array:
   - Compare characters with current prefix
   - Truncate prefix where characters don't match
   - If prefix becomes empty, return empty string
4. Return final prefix

Time complexity: O(S) where S is sum of all characters in all strings
Space complexity: O(1) - we only store the prefix string

## Alternative approach (Sort first)
1. If array is empty, return empty string
2. Sort the array of strings
3. Compare just first and last strings
   - These will have the least in common
   - Any common prefix between these is common to all
4. Return the common prefix found

Time complexity: O(n log n) for sorting + O(m) for comparison where m is length of shortest string
Space complexity: O(1) - we only store the prefix string

## Brute force approach (not recommended)
1. For each character position i:
   - Check if all strings have length > i
   - Check if all strings have same character at position i
   - If not, return prefix up to i
2. Continue until any string ends or mismatch found

Time complexity: O(S) where S is sum of all characters in all strings
Space complexity: O(1) - we only store the prefix string
