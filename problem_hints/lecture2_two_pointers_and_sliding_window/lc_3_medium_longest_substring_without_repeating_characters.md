# 3. Longest Substring Without Repeating Characters

**Problem Link**: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Easy approach (nested loops)
1. Use two nested loops to check all possible substrings
2. For each substring, check if it has no repeating characters
3. Keep track of maximum length found
4. Return maximum length

Time complexity: O(n³) - we check all substrings and each substring check is O(n)
Space complexity: O(min(m, n)) - we store unique characters in set


## Optimized approach (sliding window)
1. Use two pointers: left and right
2. Use hash set to track characters in current window
3. Expand right pointer until we find a duplicate
4. Contract left pointer until no duplicates
5. Update maximum length after each expansion

Time complexity: O(n) - we iterate through string once
Space complexity: O(min(m, n)) - we store unique characters in set


## Key insight
We can use a sliding window approach where we expand the window until we encounter a duplicate character, then contract the window from the left until we remove the duplicate. This ensures we always have a valid substring and can find the longest one efficiently. 