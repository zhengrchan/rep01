from sort import Sort

class InsertSort(Sort):
    
    def insert_sort(self):
        '''
        Sort the list
        and calculate the compare times as well as jump times 
        
        input: list
        store: self.compare_time, self.jump_time
        '''
        list = self.list
        lenth = len(list)
        self.compare_time = 0
        self.jump_time = 0
        for i in range(1, lenth):
            flag = list[i]
            j = i - 1
            while list[j] > flag and j >= 0:
                list[j], list[j+1] = list[j+1], list[j]
                self.compare_time += 1
                self.jump_time += 1
                j -= 1