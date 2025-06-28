# 15. 3Sum

**Problem Link**: https://leetcode.com/problems/3sum/

## Easy approach (three nested loops)
1. Use three nested loops to check all possible triplets
2. For each triplet, check if sum equals zero
3. Sort each triplet and add to set to avoid duplicates
4. Convert set back to list and return

Time complexity: O(n³) - three nested loops
Space complexity: O(n) - we store unique triplets


## Optimized approach (sorting + two pointers) (This is n time two sum sorted)
1. Sort the array first
2. Fix first element and use two pointers for remaining two elements
3. Use left pointer at i+1 and right pointer at end
4. If sum < 0, move left pointer right
5. If sum > 0, move right pointer left
6. If sum == 0, add triplet and skip duplicates
7. Skip duplicates for first element too

Time complexity: O(n²) - we fix one element and use two pointers
Space complexity: O(n) - we store unique triplets


## Key insight
By sorting the array first, we can use two pointers to find pairs that sum to a target value. For each fixed element, we need to find two other elements that sum to the negative of the fixed element. The sorting helps us avoid duplicates and makes the two-pointer approach efficient. 