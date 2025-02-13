class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        mapper = [0]*26
        for c1,c2 in zip(s, t):
            mapper[ord(c1)-ord('a')] +=1
            mapper[ord(c2)-ord('a')] -= 1

        # Check if every value is 0 or not
        for num in mapper:
            if num != 0:
                return False
        return True