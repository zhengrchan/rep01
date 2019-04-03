import numpy as np
from sort import Sort

class MergeSort(Sort):

    def merge_sort(self):
        self.list = self.mergesort(self.list)
        return

    def mergesort(self, list):
        '''        
        Sort the list
        and calculate the compare times as well as jump times 
        
        input: list
        store: self.compare_time, self.jump_time
        '''
        if len(list) <= 1:
            return list
        mid = len(list) // 2     
        left = self.mergesort(list[:mid])   
        right = self.mergesort(list[mid:])
        m_list = self._merge(left, right)
        return m_list
        # left, left_compare_time, left_jump_time = self.mergesort(list[:mid])
        # right, right_compare_time, right_jump_time = self.mergesort(list[mid:])
        # m_list, m_compare_time, m_jump_time = self._merge(left, right)
        # self.compare_time = left_compare_time + right_compare_time + m_compare_time
        # self.jump_time = left_jump_time + right_jump_time + m_jump_time        

    def _merge(self, left, right):
        m_list = []
        i, j = 0, 0
        while np.logical_and(i < len(left), j < len(right)):
            self.compare_time += 2
            if left[i] <= right[j]:
                self.compare_time += 1
                m_list.append(left[i])
                i += 1
                self.jump_time += 1
            else:
                self.compare_time += 1
                m_list.append(right[j])
                j += 1
                self.jump_time += 1
            
        m_list.extend(left[i:])
        m_list.extend(right[j:])
        self.jump_time += 1
        return m_list
        

