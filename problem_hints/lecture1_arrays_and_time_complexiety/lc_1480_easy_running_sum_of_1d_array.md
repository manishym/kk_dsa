# 1480. Running Sum of 1d Array

**Problem Link**: https://leetcode.com/problems/running-sum-of-1d-array/

## Easy approach (with extra space)
1. Create a new array of same size
2. Set first element of new array to first element of input array
3. For each subsequent element, add current element to previous sum
4. Store running sum in new array
5. Return new array

Time complexity: O(n) - we iterate through array once
Space complexity: O(n) - we use extra array


## In-place approach
1. Start from second element (index 1)
2. Add current element to previous element in the same array
3. Continue until end of array
4. Return modified array

Time complexity: O(n) - we iterate through array once
Space complexity: O(1) - we modify array in-place


## Key insight
A running sum is just the cumulative sum of all previous elements. We can compute this by adding each element to the sum of all previous elements. The in-place approach works because we only need the previous element's value to compute the current running sum. 