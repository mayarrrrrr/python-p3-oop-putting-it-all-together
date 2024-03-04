#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size
        
        
        
    @property
    def size(self):
        return self._page_count
    
    @size.setter
    def size(self,size):
        if type(size)== int :
            self._page_count = size
        else:
            print("size must be an integer") 
            
    def cobble(self): 
        self.condition = "New"
        print( "Your shoe is as good as new!")  
        
    
                   
        pass