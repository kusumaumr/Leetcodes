class Solution(object):
    def isValid(self, s):
        va=[]
        ch_val=True
        for ch in s:
            if ch in "{([":
                va.append(ch)
            else:
                if len(va)!=0:
                    if(ch=="]" and va[-1]=='[' or  (ch==")" and va[-1]=='(') or (ch=="}" and va[-1]=='{')):
                        va.pop()
                    else:
                        ch_val=False
                else:
                    ch_val=False
                    break
        if len(va)!=0:
            ch_val=False  
                 
        return ch_val
                