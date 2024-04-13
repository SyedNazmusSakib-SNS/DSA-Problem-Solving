"""
## Question
### 1395. [Count Number of Teams](https://leetcode.com/problems/count-number-of-teams/)
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:
(rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4


Constraints:
n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5
"""

## Solutions


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        i = 0
        while i < len(rating) - 2:
            j = i + 1
            while j < len(rating) - 1:
                k = j + 1
                while k < len(rating):
                    if (rating[i] < rating[j] < rating[k]) or (
                        rating[i] > rating[j] > rating[k]
                    ):
                        count += 1
                    k += 1
                j += 1
            i += 1
        return count


# Runtime: 2256 ms, faster than 50.00% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions
