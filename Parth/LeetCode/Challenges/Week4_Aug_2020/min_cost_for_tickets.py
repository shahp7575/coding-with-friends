from typing import List

class Solution:

    """
    Problem Statement:

    """

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        len_days = len(days)
        cost_ones = len_days*costs[0]
        day_range = 7

        for i in days:
            last_day = days[0] + (day_range - 1)
            if i > to_add:
                days = 

        return cost_ones


if __name__ == "__main__":

    result = Solution()
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    print(result.mincostTickets(days, costs))