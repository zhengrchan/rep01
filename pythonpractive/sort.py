import time

class Sort(object):
    '''
    Base class for sort
    '''
    def __init__(self, list):
        self.list = list
        self.compare_time = 0
        self.jump_time = 0
        self.run_time = 0

    def time(self, func):
        '''
        Calculate the running time of func()
        and then store in the self.run_time
        '''
        start = time.time()
        func()
        end = time.time()
        self.run_time = end - start

