# 88. Merge Sorted Array

**Problem Link**: https://leetcode.com/problems/merge-sorted-array/

## Easy approach (with extra space)
1. Create a new array of size m + n
2. Use two pointers to merge arrays in sorted order
3. Copy elements from both arrays to new array
4. Copy new array back to nums1

Time complexity: O(m + n) - we iterate through both arrays
Space complexity: O(m + n) - we use extra array


## In-place approach (from end)
1. Use three pointers: p1 at end of nums1, p2 at end of nums2, p at end of result
2. Compare elements from end and place larger one at end
3. Move pointer backward for the array we took element from
4. Continue until we've placed all elements

Time complexity: O(m + n) - we iterate through both arrays
Space complexity: O(1) - we modify array in-place


## Key insight
By merging from the end of the arrays, we avoid overwriting elements in nums1 that we still need. This allows us to merge in-place without extra space, since the end of nums1 is already filled with zeros. 