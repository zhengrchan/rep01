import time
from sort import Sort

class QuickSort(Sort):

    def quick_sort(self):
        '''
        Sort the list
        and calculate the compare times as well as jump times 
        
        '''
        self._quicksort(self.list, 0, len(self.list)-1)
        return
    
    def _quicksort(self, list, start, end):
        '''
        Sort the list
        and calculate the compare times as well as jump times 
        
        '''
        if start >= end:
            self.compare_time += 1
            return list, 1, 0
        else: 
            self.compare_time += 1
        
        # partition
        key = list[end]
        i = start - 1
        for j in range(start, end):
            if list[j] < key:
                i += 1
                list[i], list[j] = list[j], list[i]
                self.compare_time += 1
                self.jump_time += 1
            else:
                self.compare_time += 1
        list[i+1], list[end] = list[end], list[i+1]
        self.jump_time += 1

        self._quicksort(list, start, i)
        self._quicksort(list, i + 2, end)





    
    


