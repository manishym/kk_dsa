# 26. Remove Duplicates from Sorted Array

**Problem Link**: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


## In-place approach (two pointers)
1. Use two pointers: one for reading (i), one for writing (j)
2. Start both pointers at index 1 (since first element is always unique)
3. Compare current element with previous element
4. If different, copy current element to write position and increment write pointer
5. Always increment read pointer
6. Return write pointer position (number of unique elements)

Time complexity: O(n) - we iterate through array once
Space complexity: O(1) - we modify array in-place


## Key insight
Since the array is sorted, duplicates will always be adjacent. We can use a two-pointer technique where one pointer reads through the array and another pointer writes unique elements. The write pointer only moves when we encounter a new unique element. 