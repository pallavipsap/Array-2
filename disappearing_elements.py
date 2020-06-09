# May 8 2020
# Python solution

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Time complexity : O(n)
        # If we have two sets of lenth m and n, time complexity will be equal to O(smaller set length)

        # Space complexity : O(len(nums))
        # We need maximum sapce of length of the nums ( smaller set ) for comparison between bigger set and smaller set

        '''
        The idea of sets came into the mind, because we are trying to find elements which are uncommon to both
        So set intersection, set union, set difference these operations were thought of by drawing venn diagram.
        small set = set of the given list, big is [1,n]
        set intersection [ big - small ] gives all the elements uncommmon in big and small set , present in big
        Considering big set contains all the elements from [1 , n]  inclusive, big - small was considered and not
        small - big, basically small is a subset of big
        Again, I am mentioning a subset because a test case : [1,8] ==> where big = {1,2}, small = {1,8} is invalid.
        Because here small is not a subset of big

        '''
        # works in leet code sum #448

        if len(nums) == 0: return []

        maximum = len(nums)
        l = [n for n in range(1, maximum + 1)]

        given_set = set(nums)
        big_set = set(l)
        print(big_set)
        print(given_set)
        res = []
        print(big_set.difference(given_set))  # big_set - given_set

        return list(big_set.difference(given_set))

