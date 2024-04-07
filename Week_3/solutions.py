class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        maxCandies = max(candies)
        result = []
        for candy in range(len(candies)):
            result.append(candies[candy] + extraCandies >= maxCandies)
        return result
