# 11. Container With Most Water

**Problem Link**: https://leetcode.com/problems/container-with-most-water/

## Optimized approach (two pointers)
1. Use two pointers: left at start, right at end
2. Calculate area with current two lines
3. Move pointer with smaller height inward
4. Update maximum area if current area is larger
5. Continue until pointers meet

Time complexity: O(n) - we only need one pass
Space complexity: O(1) - we only store maximum area


## Key insight
The area is limited by the shorter of the two lines. By starting with the widest possible container (leftmost and rightmost lines), we can eliminate many combinations. If we move the pointer with the taller line inward, the area can only decrease because the width decreases and the height is still limited by the shorter line. 