# 125. Valid Palindrome

**Problem Link**: https://leetcode.com/problems/valid-palindrome/

## Easy approach (with extra space)
1. Create a new string with only alphanumeric characters
2. Convert to lowercase
3. Compare string with its reverse
4. Return true if they match

Time complexity: O(n) - we iterate through string once
Space complexity: O(n) - we create new string


## Two pointers approach
1. Use two pointers: left at start, right at end
2. Skip non-alphanumeric characters from both ends
3. Compare characters (case-insensitive)
4. Move pointers inward if they match
5. Return false if they don't match

Time complexity: O(n) - we iterate through string once
Space complexity: O(1) - we only use two pointers


## Key insight
A palindrome reads the same forward and backward. By using two pointers from both ends and skipping non-alphanumeric characters, we can check if the string is a palindrome without creating extra space. We only need to compare characters until the pointers meet in the middle. 