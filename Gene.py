import random

class Gene:
    def __init__(self, age):
        self.age = age
        self.is_dominant = bool(random.randint(0, 1))
        self.theoretical_desirability = random.randint(0, 100)
    
    def get_age(self):
        return self.age

    def get_dominance(self):
        return self.is_dominant
    
    def get_desirability(self):
        return self.theoretical_desirability
    
