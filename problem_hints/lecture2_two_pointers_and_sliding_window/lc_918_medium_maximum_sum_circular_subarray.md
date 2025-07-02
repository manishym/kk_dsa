# 918. Maximum Sum Circular Subarray

**Problem Link**: https://leetcode.com/problems/maximum-sum-circular-subarray/

## Easy approach (check all circular subarrays)
1. Consider array as circular by duplicating it
2. Use two nested loops to check all possible circular subarrays
3. Calculate sum for each subarray
4. Keep track of maximum sum found
5. Return maximum sum

Time complexity: O(n²) - we check all possible circular subarrays
Space complexity: O(1) - we only store maximum sum


## Optimized approach (Kadane's algorithm + min subarray)
1. Find maximum subarray sum using Kadane's algorithm
2. Find minimum subarray sum using modified Kadane's
3. Calculate total sum of array
4. Return max(max_subarray, total_sum - min_subarray)
5. Handle case where all elements are negative

Time complexity: O(n) - we iterate through array twice
Space complexity: O(1) - we only use a few variables


## Key insight
The maximum circular subarray sum is either the maximum subarray sum (non-circular) or the total sum minus the minimum subarray sum (circular). This is because the circular part wraps around the array, so we can think of it as removing the minimum subarray from the total. 