import random

class Gene:
    def __init__(self, lifespan):
        self.lifespan = lifespan
        self.is_dominant = bool(random.randint(0, 1))
        self.theoretical_desirability = random.randint(0, 100)
    
    def get_lifespan(self):
        return self.lifespan

    def get_dominance(self):
        return self.is_dominant
    
    def get_desirability(self):
        return self.theoretical_desirability
    
