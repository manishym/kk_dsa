# 217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/description

## Easiest approach
1. What would be length of hashset of numbers compared to the numbers list?

## Easy approach (Using Set)
1. Create an empty set
2. For each number in the array:
   - If number is already in set, return True
   - If not, add number to set
3. After loop completes, return False (no duplicates found)

Time complexity: O(n) - we iterate through array once
Space complexity: O(n) - we store up to n numbers in the set


## Brute force approach (not recommended)
1. For each number at index i:
   - Check all numbers after index i
   - If any match is found, return True
2. Return False if no duplicates found

Time complexity: O(n²) - nested loops
Space complexity: O(1) - only need a few variables
