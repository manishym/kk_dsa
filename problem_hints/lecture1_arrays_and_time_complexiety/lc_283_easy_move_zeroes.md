# 283. Move Zeroes

**Problem Link**: https://leetcode.com/problems/move-zeroes/


## In-place approach (two pointers)
1. Use two pointers: one for reading (i), one for writing (j)
2. Both pointers start at index 0
3. When we encounter non-zero element, copy it to write position and increment write pointer
4. Always increment read pointer
5. After first pass, fill remaining positions with zeros

Time complexity: O(n) - we iterate through array once
Space complexity: O(1) - we modify array in-place


## Key insight
We can use the same two-pointer technique as "Remove Duplicates from Sorted Array". The write pointer keeps track of where to place the next non-zero element, while the read pointer scans through the array. After placing all non-zeros, we fill the remaining positions with zeros. 