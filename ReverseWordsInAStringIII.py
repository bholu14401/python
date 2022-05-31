class Solution(object):
    def reverseWords(self, s):
        
        s = s.split()
        y=''
        for x in s:
            if x=='':
                continue
                y.append(x)            
            else:
                x = x[::-1]
            y = y +" "+  x
        return y.strip()
     
        
