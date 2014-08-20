class Clue(object):

    def __init__(self,value):
        self.value = value
        self.status = "to_solve"
        
    # Setter
    
    def solve(self):
        self.status = "solved"
        
    # Getter
    
    def is_solved(self):
        return self.status == "solved"
        
    def get_value(self):
        return self.value
        
    # Representation

    def __str__(self):
        return str(self.value)
