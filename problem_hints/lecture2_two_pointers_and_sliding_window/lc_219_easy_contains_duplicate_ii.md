# 219. Contains Duplicate II

**Problem Link**: https://leetcode.com/problems/contains-duplicate-ii/

## Easy approach (nested loops)
1. Use two nested loops to check all pairs
2. For each pair, check if values are equal and indices differ by at most k
3. Return true if such pair is found
4. Return false if no such pair exists

Time complexity: O(n²) - we check all possible pairs
Space complexity: O(1) - we only use a few variables


## Optimized approach (sliding window + hash set)
1. Use a hash set to store elements in current window
2. Window size is k + 1 (indices can differ by at most k)
3. For each element, check if it exists in current window
4. If yes, return true
5. Add current element to window and remove oldest if window is full

Time complexity: O(n) - we iterate through array once
Space complexity: O(k) - we store at most k elements in set


## Key insight
We can use a sliding window approach with a hash set. The window contains at most k + 1 elements, and if we find a duplicate within this window, it means the indices differ by at most k. This is more efficient than checking all pairs. 