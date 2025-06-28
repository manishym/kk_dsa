# 42. Trapping Rain Water

**Problem Link**: https://leetcode.com/problems/trapping-rain-water/

## Easy approach (with extra space)
1. Create two arrays: left_max and right_max
2. Fill left_max: left_max[i] = max height from index 0 to i
3. Fill right_max: right_max[i] = max height from index i to n-1
4. For each position, water trapped = min(left_max[i], right_max[i]) - height[i]
5. Sum all trapped water

Time complexity: O(n) - we iterate through array three times
Space complexity: O(n) - we use two extra arrays


## Optimized approach (right max array)
1. Create right_max array: right_max[i] = max height from index i to n-1
2. Keep track of left_max as we iterate from left to right
3. For each position, water trapped = min(left_max, right_max[i]) - height[i]
4. Update left_max = max(left_max, height[i])
5. Sum all trapped water

Time complexity: O(n) - we iterate through array twice
Space complexity: O(n) - we use one extra array


## Key insight
We only need to store the right maximum array. As we iterate from left to right, we can keep track of the left maximum on-the-fly. This reduces the space complexity from two arrays to one array while maintaining the same time complexity. 