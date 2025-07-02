# 53. Maximum Subarray

**Problem Link**: https://leetcode.com/problems/maximum-subarray/

## Easy approach (nested loops)
1. Use two nested loops to check all possible subarrays
2. For each subarray, calculate sum
3. Keep track of maximum sum found
4. Return maximum sum

Time complexity: O(n²) - we check all possible subarrays
Space complexity: O(1) - we only store maximum sum


## Optimized approach (Kadane's algorithm)
1. Use two variables: current_sum and max_sum
2. Initialize current_sum = nums[0], max_sum = nums[0]
3. For each element, current_sum = max(nums[i], current_sum + nums[i])
4. Update max_sum = max(max_sum, current_sum)
5. Return max_sum

Time complexity: O(n) - we iterate through array once
Space complexity: O(1) - we only use two variables


## Key insight
Kadane's algorithm works because if we have a negative sum, it's better to start fresh from the current element rather than carrying forward the negative sum. This is because any positive number is better than a negative number when we're trying to maximize the sum. 