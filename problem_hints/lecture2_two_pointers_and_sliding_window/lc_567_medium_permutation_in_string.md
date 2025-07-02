# 567. Permutation in String

**Problem Link**: https://leetcode.com/problems/permutation-in-string/

## Easy approach (check each window)
1. For each possible starting position, check if substring is permutation
2. Sort both strings and compare
3. Return true if any match is found
4. Return false if no match

Time complexity: O(n * m * log m) - we check each window and sort
Space complexity: O(m) - we store sorted strings


## Optimized approach (sliding window + frequency count)
1. Create frequency arrays for s1 and current window
2. Use sliding window of size equal to s1 length
3. Compare frequency arrays to check if they match
4. Return true if frequencies match
5. Update frequency arrays as window slides

Time complexity: O(n) - we iterate through string once
Space complexity: O(26) - we store frequency count for each character


## Key insight
This is similar to "Find All Anagrams in a String" but we only need to find one match. We can use the same sliding window approach with frequency counting to efficiently check if any window is a permutation of s1. 