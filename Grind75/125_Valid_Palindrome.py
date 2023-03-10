class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(len(s) == 1):
            return True

        letters_only = ""

        for char in s:
            if char.isalpha() or char.isdigit():
                letters_only += char.lower()
        
        lp = 0
        rp = len(letters_only) - 1


        while(lp < rp):
            if letters_only[lp] != letters_only[rp]:
                return False
            lp += 1
            rp -= 1
        
        return True

if __name__ == "__main__":
    solution = Solution()
    s1 = "A man, a plan, a canal: Panama" #True
    s2 = "race a car" #False
    print(solution.isPalindrome(s1))
    print(solution.isPalindrome(s2))