class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        str1=''
        for i in s:
            if i.isdigit() or i.isalpha():
                str1+=i
        return str1 == str1[::-1]