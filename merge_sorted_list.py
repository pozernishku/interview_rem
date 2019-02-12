class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        i, j = 0, 0
        
        if m == 0:
            nums1.clear()
            nums1.extend(nums2)
            return
            
        while n > j:
            cur_n1, cur_n2 = nums1[i], nums2[j]
            next_n1 = nums1[i+1] if i+1 < m else None
            
            if cur_n2 >= cur_n1:
                if next_n1 is not None and cur_n2 >= next_n1:
                    i += 1
                else:
                    i += 1
                    nums1.insert(i, cur_n2)
                    nums1.pop(-1)
                    m += 1
                    j += 1
            else:
                nums1.insert(i, cur_n2)
                nums1.pop(-1)
                j += 1
                m += 1