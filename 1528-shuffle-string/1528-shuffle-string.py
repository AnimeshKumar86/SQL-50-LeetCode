class Solution(object):
    def restoreString(self, s, indices):
        s_list = list(s)
        i = 0
        while i < len(s_list):
            correct_pos = indices[i]
            
            if correct_pos != i:
                s_list[i], s_list[correct_pos] = s_list[correct_pos], s_list[i]
                indices[i], indices[correct_pos] = indices[correct_pos], indices[i]
            else:
                i += 1
                
        return "".join(s_list)