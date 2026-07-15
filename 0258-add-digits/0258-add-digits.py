class Solution(object):
    def addDigits(self, num):
        while(num>=10):
            sum=0
            while(num>0):
                r=num%10
                sum+=r
                num//=10
            num=sum
        return num
                

        
        
            