# super class 
class Shape: 
      
    # constructor 
    def __init__(self, length, breadth): 
        self._length = length
        self._breadth = breadth 
          
    # public member function 
    def displaySides(self): 
  
        # accessing protected data members 
        print("Length: ", self._length) 
        print("Breadth: ", self._breadth) 


print(Shape('a','b')._length)