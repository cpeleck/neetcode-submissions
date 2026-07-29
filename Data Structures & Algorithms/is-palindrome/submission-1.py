class Solution:
    def isPalindrome(self, s: str) -> bool:
        curr_str = ''.join(filter(str.isalnum, s)).lower()
        if len(curr_str) == 0:
            return True
        left_pointer_idx = 0
        left_pointer = curr_str[left_pointer_idx]
        right_pointer_idx = len(curr_str) - 1
        right_pointer = curr_str[right_pointer_idx]
        while right_pointer_idx > left_pointer_idx:
            if left_pointer != right_pointer:
                return False
            left_pointer_idx += 1
            right_pointer_idx -= 1
            left_pointer = curr_str[left_pointer_idx]
            right_pointer = curr_str[right_pointer_idx]

        return True


    