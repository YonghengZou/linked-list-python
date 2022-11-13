class EmptyException(Exception):
    def __init__(self): 
        super().__init__(message="Link list empty")
class IndexOutOfBound(Exception):
    def __init__(self): 
        super().__init__(message="Index out of bound")