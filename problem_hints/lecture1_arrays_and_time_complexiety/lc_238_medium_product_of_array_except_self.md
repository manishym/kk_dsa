# 238. Product of Array Except Self

**Problem Link**: https://leetcode.com/problems/product-of-array-except-self/

## Easy approach (with extra space)
1. Create two arrays: left and right
2. Fill left array: left[i] = product of all elements from index 0 to i-1
3. Fill right array: right[i] = product of all elements from index i+1 to n-1
4. answer[i] = left[i] * right[i]
5. Done

Time complexity: O(n) - we iterate through array three times
Space complexity: O(n) - we use two extra arrays


## Space optimized approach
1. Use answer array to store left products first
2. Then use a single variable to keep track of right products
3. Update answer array from right to left


Time complexity: O(n)
Space complexity: O(1) - excluding output array


## Key insight
The product except self can be broken down into:
- Left product: Product of all elements to the left of current position
- Right product: Product of all elements to the right of current position
- Final answer: Left product × Right product

This avoids using division (which is not allowed) and gives us O(n) time complexity.
