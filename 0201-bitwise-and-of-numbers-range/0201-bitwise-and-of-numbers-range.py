class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        # res=0
        while(left<right):
            right=right&right-1

        return right
