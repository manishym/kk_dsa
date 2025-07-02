# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

**Problem Link**: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

## Easy approach (check each window)
1. For each possible starting position, calculate sum of k elements
2. Calculate average and compare with threshold
3. Increment count if average >= threshold
4. Return total count

Time complexity: O(n * k) - we check each window and calculate sum
Space complexity: O(1) - we only store count


## Optimized approach (sliding window)
1. Calculate sum of first k elements
2. Check if average >= threshold and increment count
3. For each subsequent window, subtract first element and add new element
4. Check average and increment count if >= threshold
5. Return total count

Time complexity: O(n) - we iterate through array once
Space complexity: O(1) - we only store sum and count


## Key insight
We can use a sliding window approach where we maintain the sum of k consecutive elements. For each new window, we subtract the first element of the previous window and add the new element, avoiding recalculating the entire sum. 