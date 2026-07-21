class Solution(object):
    def hasAlternatingBits(self, n):
        l=[]
        var=n
        while(n!=0):
            var=n%2
            l.append(var)
            n=n//2
            

        for i in range(1,len(l)):
            if(l[i-1]==l[i]):
                return False
        return True       