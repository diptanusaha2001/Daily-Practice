class Solution:
    def numberOfSubstrings(self, s: str) -> int:
  
        ca=0  
        cb=0   
        cc=0 
        ans=0 
        j=0 
        
        for i in range(len(s)):
            if s[i]=='a': 
                ca+=1
            elif s[i]=='b':
                cb+=1
            else: 
                cc+=1
                
            while ca>0 and cb>0 and cc>0: 
                ans+=len(s)-i   
                if s[j]=='a':
                    ca-=1
                elif s[j]=='b':
                    cb-=1
                else:
                    cc-=1 
                j+=1 
                if j==len(s):
                    return ans 
        return ans
        
