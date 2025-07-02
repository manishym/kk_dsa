# 438. Find All Anagrams in a String

**Problem Link**: https://leetcode.com/problems/find-all-anagrams-in-a-string/

## Easy approach (check each window)
1. For each possible starting position, check if substring is anagram
2. Sort both strings and compare
3. Add starting index to result if they match
4. Return all starting indices

Time complexity: O(n * m * log m) - we check each window and sort
Space complexity: O(m) - we store sorted strings


## Optimized approach (sliding window + frequency count)
1. Create frequency arrays for pattern and current window
2. Use sliding window of size equal to pattern length
3. Compare frequency arrays to check if they match
4. Add starting index to result if frequencies match
5. Update frequency arrays as window slides

Time complexity: O(n) - we iterate through string once
Space complexity: O(26) - we store frequency count for each character


## Key insight
Two strings are anagrams if they have the same character frequencies. We can use a sliding window approach with frequency counting to efficiently check if each window is an anagram of the pattern, avoiding the need to sort strings. 