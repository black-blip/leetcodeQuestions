class Solution(object):
    def commonprefixyet(self,str1,str2):
        i,j = 0,0
        res = ''
        n1,n2 = len(str1),len(str2)
        while i<=n1-1 and j<=n2-1:
            if (str1[i]!=str2[j]):
                break
            res+=str1[i]
            i+=1
            j+=1
        return res
        
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for i in range(1,len(strs)):
            prefix = self.commonprefixyet(prefix,strs[i])
            
        return prefix
