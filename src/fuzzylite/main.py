'''
Created on 10/10/2012

@author: jcrada
'''

class Something:
    
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        print('next called')
        if self.n > 10: raise StopIteration
        self.n += 1
        return self.n

if __name__ == '__main__':
    x = Something(0)
    for i in x:
        print('loop')