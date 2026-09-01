class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = defaultdict(int)
        s2_hash = defaultdict(int)
        for letter in s1:
            s1_hash[letter] += 1
            
        
        l = 0
        r = len(s1) - 1
        while r < len(s2):
            window = s2[l:r+1]
            for letter in window:
                s2_hash[letter] += 1
            is_match = True
            for entry in s1_hash:
                if s2_hash[entry] != s1_hash[entry]:
                    is_match = False
            if is_match:
                return True
            s2_hash = defaultdict(int)
                
            l += 1
            r += 1
        return False



        