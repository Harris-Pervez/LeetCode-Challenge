class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=""
        for i in s:
            if i.isalpha():
                c+=i.lower()
            elif i.isnumeric():
                c+=i
        return c==c[::-1]
        
        