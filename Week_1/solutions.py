class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):  # Checks the amount of numbers in the array and iterates i through them
            # j starts from the next number from where i is and iterates theough the length of numbers in i
            for j in range(i+1, len(nums)):
                # Adds the number in i and j and then compares it to the target value,
                if nums[i] + nums[j] == target:
                    # If true, it prints the position of the two values in the array
                    return [i, j]
        return []
