class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        strs.sort(key=len,reverse=False)
        substr=strs[0]
        while(substr>0):
            status=True
            for i in range(0,len(strs)):
                if substr not in strs[i] or strs[i].find(substr)!=0:
                    status=False
                    break
            if(status==False):
                substr=substr[0:len(substr)-1]
            else:
                break
        
        return substr


        