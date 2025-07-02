# 209. Minimum Size Subarray Sum

**Problem Link**: https://leetcode.com/problems/minimum-size-subarray-sum/

## Easy approach (nested loops)
1. Use two nested loops to check all possible subarrays
2. For each subarray, calculate sum
3. If sum >= target, update minimum length
4. Return minimum length found

Time complexity: O(n²) - we check all possible subarrays
Space complexity: O(1) - we only store minimum length


## Optimized approach (sliding window)
1. Use two pointers: left and right
2. Expand right pointer and add elements to sum
3. When sum >= target, contract left pointer and subtract elements
4. Update minimum length after each contraction
5. Continue until right pointer reaches end

Time complexity: O(n) - we iterate through array once
Space complexity: O(1) - we only use two pointers and sum


## Key insight
We can use a sliding window approach where we expand the window until the sum is >= target, then contract the window from the left to find the minimum length. This ensures we find the shortest subarray that meets the target sum requirement. 