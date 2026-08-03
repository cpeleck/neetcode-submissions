class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = list(s)
        t_list = list(t)
        s_dict = dict()
        t_dict = dict()
    
        for letter in s_list:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        for letter in t_list:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1
        
        for s_entry in s_dict.keys():
            try:
                if s_dict[s_entry] == t_dict[s_entry]:
                    continue
                else:
                    return False
            except:
                return False
        return True


