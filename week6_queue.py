
class Queue(object):
    ''' Create a queue'''
    def __init__(self):
        ''' creates empty list of items'''
        self.vals = []
        
    def insert(self, item):
        ''' insert item into the end the queue'''
        self.vals.append(item)
        
    def remove(self):
        ''' remove item from the front of the list
            raises error if list is empty'''
        try:
            return self.vals.pop()
        except:
            raise ValueError()
        
        
    