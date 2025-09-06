#https://leetcode.com/problems/find-closest-person/description/?envType=daily-question&envId=2025-09-04
class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """

        if x == y:
            return 0
        elif abs(x - z) < abs(y - z):
            return 1
        elif abs(x - z) > abs(y - z):
            return 2
        else:
            return 0