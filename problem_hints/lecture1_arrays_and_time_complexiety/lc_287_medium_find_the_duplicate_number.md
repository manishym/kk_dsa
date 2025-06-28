# 287. Find the Duplicate Number

**Problem Link**: https://leetcode.com/problems/find-the-duplicate-number/

## Easy approach
1. Create a set
1. for each number in the array, check if number is in set.
   - If number is in set, return number
   - If not, add number to set
2. Done
Time complexity: O(n) - we iterate through array once
Space complexity: O(n) - we store up to n numbers in the set


## Hare and tortoise approach (will discuss this when we solve linked lists.)
1. The hare and tortoise (Floyd's cycle detection) approach treats the array as a linked list:
   - For each index i, the "next" node is at index nums[i]
   - Since there's a duplicate number, this creates a cycle in the "linked list"

2. Use two pointers moving at different speeds:
   - Tortoise moves one step at a time: tortoise = nums[tortoise]
   - Hare moves two steps at a time: hare = nums[nums[hare]]
   
3. They will eventually meet inside the cycle
   - Let's say distance from start to cycle entry is x
   - Distance from cycle entry to meeting point is y
   - Remaining cycle distance is z
   - When they meet: tortoise traveled x + y steps
   - Hare traveled x + y + n(y + z) steps where n is some integer
   - Since hare moves 2x faster: 2(x + y) = x + y + n(y + z)
   - This means x = n(y + z) - y = (n-1)(y + z) + z
   
4. After they meet:
   - Reset one pointer to start
   - Move both pointers one step at a time
   - They will meet at cycle entry point (the duplicate number)
   - This works because x = (n-1)(y + z) + z

Time complexity: O(n)
Space complexity: O(1)

