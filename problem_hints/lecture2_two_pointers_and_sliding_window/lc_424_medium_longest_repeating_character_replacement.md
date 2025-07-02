# 424. Longest Repeating Character Replacement

**Problem Link**: https://leetcode.com/problems/longest-repeating-character-replacement/

## Easy approach (nested loops)
1. Use two nested loops to check all possible substrings
2. For each substring, count frequency of each character
3. Find character with maximum frequency
4. If (length - max_freq) <= k, update maximum length
5. Return maximum length found

Time complexity: O(n² * 26) - we check all substrings and count frequencies
Space complexity: O(26) - we store frequency count for each character


## Optimized approach (sliding window)
1. Use two pointers: left and right
2. Use array to count frequency of characters in current window
3. Track maximum frequency in current window
4. If (window_size - max_freq) > k, contract left pointer
5. Update maximum length after each expansion

Time complexity: O(n) - we iterate through string once
Space complexity: O(26) - we store frequency count for each character


## Key insight
We can use a sliding window approach where we expand the window until we can't make more than k replacements, then contract the window from the left. The key insight is that we only need to track the maximum frequency in the current window, not all frequencies. 